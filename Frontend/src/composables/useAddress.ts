import { ref } from 'vue';
import axios from 'axios';

export interface AddressData {
  cep: string;
  logradouro: string;
  complemento: string;
  bairro: string;
  localidade: string;
  uf: string;
  ibge: string;
  gia: string;
  ddd: string;
  siafi: string;
  erro?: boolean;
}

export function useAddress() {
  const loading = ref(false);
  const error = ref('');

  const fetchAddress = async (cep: string): Promise<AddressData | null> => {
    const cleanCep = cep.replace(/\D/g, '');
    if (cleanCep.length !== 8) {
      error.value = 'CEP inválido';
      return null;
    }

    loading.value = true;
    error.value = '';

    try {
      const response = await axios.get<AddressData>(`https://viacep.com.br/ws/${cleanCep}/json/`);
      if (response.data.erro) {
        error.value = 'CEP não encontrado';
        return null;
      }
      return response.data;
    } catch (err) {
      error.value = 'Erro ao buscar o CEP';
      return null;
    } finally {
      loading.value = false;
    }
  };

  return { fetchAddress, loading, error };
}
