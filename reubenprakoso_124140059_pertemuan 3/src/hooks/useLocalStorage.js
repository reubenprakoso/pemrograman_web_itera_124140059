
import { useState } from 'react'

export default function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try {
      const savedValue = localStorage.getItem(key)
      return savedValue !== null
        ? JSON.parse(savedValue)
        : initialValue
    } catch (error) {
      console.error('Gagal membaca localStorage:', error)
      return initialValue
    }
  })

  function updateValue(newValue) {
    setValue((currentValue) => {
      const nextValue =
        typeof newValue === 'function'
          ? newValue(currentValue)
          : newValue

      try {
        localStorage.setItem(key, JSON.stringify(nextValue))
      } catch (error) {
        console.error('Gagal menyimpan localStorage:', error)
      }

      return nextValue
    })
  }

  return [value, updateValue]
}
