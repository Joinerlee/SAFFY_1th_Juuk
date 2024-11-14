<template>
  <div class="exchange-calculator">
    <h2>환율 계산기</h2>
    <div v-if="exchangeStore.loading">로딩 중...</div>
    <div v-else-if="exchangeStore.error">{{ exchangeStore.error }}</div>
    <div v-else>
      <div>
        <input v-model.number="amount" type="number" placeholder="금액">
        <select v-model="fromCurrency">
          <option v-for="currency in exchangeStore.availableCurrencies" :key="currency">{{ currency }}</option>
        </select>
      </div>
      <div>
        <input :value="convertedAmount" type="number" readonly>
        <select v-model="toCurrency">
          <option v-for="currency in exchangeStore.availableCurrencies" :key="currency">{{ currency }}</option>
        </select>
      </div>
      <p>1 {{ fromCurrency }} = {{ exchangeRate }} {{ toCurrency }}</p>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useExchangeStore } from '../stores/exchange'

export default {
  setup() {
    const exchangeStore = useExchangeStore()
    const amount = ref(1)
    const fromCurrency = ref('USD')
    const toCurrency = ref('KRW')

    const exchangeRate = computed(() => {
      if (!exchangeStore.rates[fromCurrency.value] || !exchangeStore.rates[toCurrency.value]) return 0
      return (exchangeStore.rates[toCurrency.value] / exchangeStore.rates[fromCurrency.value]).toFixed(4)
    })

    const convertedAmount = computed(() => {
      return (amount.value * exchangeRate.value).toFixed(2)
    })

    onMounted(() => {
      exchangeStore.fetchRates()
    })

    return {
      exchangeStore,
      amount,
      fromCurrency,
      toCurrency,
      exchangeRate,
      convertedAmount
    }
  }
}
</script>