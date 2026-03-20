import axios from 'axios'
import { ref } from 'vue'

export function useAddress() {
    const loadingCep = ref(false)

    const fetchAddress = async (cep) => {
        const cleanCep = cep.replace(/\D/g, '')
        if (cleanCep.length !== 8) return null

        loadingCep.value = true
        try {
            const { data } = await axios.get(`https://viacep.com.br/ws/${cleanCep}/json/`)
            return data.erro ? null : data
        } catch (error) {
            console.error("Erro ao buscar CEP: ", error)
            return null
        } finally {
            loadingCep.value = false
        }
    }

    return { fetchAddress, loadingCep }
}
