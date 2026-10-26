import { render, screen, fireEvent } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import BookForm from "../components/BookForm/BookForm";

describe("BookForm", () => {
  it("menampilkan form tambah buku", () => {
    render(<BookForm onAddBook={vi.fn()} />);

    expect(
      screen.getByRole("heading", { name: "Tambah Buku" }),
    ).toBeInTheDocument();

    expect(screen.getByLabelText("Judul Buku")).toBeInTheDocument();
    expect(screen.getByLabelText("Nama Penulis")).toBeInTheDocument();
  });

  it("menampilkan pesan jika judul dan penulis kosong", () => {
    render(<BookForm onAddBook={vi.fn()} />);

    fireEvent.click(screen.getByRole("button", { name: "Tambah Buku" }));

    expect(screen.getByRole("alert")).toHaveTextContent(
      "Judul dan nama penulis wajib diisi.",
    );
  });

  it("menambahkan buku jika form diisi dengan benar", () => {
    const onAddBook = vi.fn();

    render(<BookForm onAddBook={onAddBook} />);

    fireEvent.change(screen.getByLabelText("Judul Buku"), {
      target: { value: "Laskar Pelangi" },
    });

    fireEvent.change(screen.getByLabelText("Nama Penulis"), {
      target: { value: "Andrea Hirata" },
    });

    fireEvent.click(screen.getByRole("button", { name: "Tambah Buku" }));

    expect(onAddBook).toHaveBeenCalledWith({
      title: "Laskar Pelangi",
      author: "Andrea Hirata",
      status: "owned",
    });
  });

  it("menggunakan status Sudah Dimiliki secara default", () => {
    render(<BookForm onAddBook={vi.fn()} />);

    expect(screen.getByLabelText("Status Buku")).toHaveValue("owned");
  });

  it("mengosongkan form setelah buku berhasil ditambahkan", () => {
    render(<BookForm onAddBook={vi.fn()} />);

    fireEvent.change(screen.getByLabelText("Judul Buku"), {
      target: { value: "Laskar Pelangi" },
    });

    fireEvent.change(screen.getByLabelText("Nama Penulis"), {
      target: { value: "Andrea Hirata" },
    });

    fireEvent.click(screen.getByRole("button", { name: "Tambah Buku" }));

    expect(screen.getByLabelText("Judul Buku")).toHaveValue("");
    expect(screen.getByLabelText("Nama Penulis")).toHaveValue("");
  });
});
