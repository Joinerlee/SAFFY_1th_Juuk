<template>
  <div>
    <h2>환율 계산기</h2>
    <p>금일 환율 정보를 확인해보세요.</p>

    <form @submit.prevent="fetchRates">
      <div>
        <label for="amount">환전할 금액</label>
        <input
          id="amount"
          v-model.number="amount"
          type="number"
          placeholder="금액 입력"
          min="0"
        />
      </div>

      <div>
        <label for="fromCurrency">기준 통화</label>
        <select id="fromCurrency" v-model="fromCurrency">
          <option value="KRW">KRW (원)</option>
          <option value="USD">USD (달러)</option>
          <option value="EUR">EUR (유로)</option>
          <option value="JPY">JPY (엔)</option>
        </select>
      </div>

      <button type="submit" :disabled="loading">
        {{ loading ? '계산 중...' : '환율 계산' }}
      </button>
    </form>

    <div v-if="error" class="error">
      {{ error }}
    </div>

    <div v-if="rates" class="results">
      <h3>환율 정보</h3>
      <ul>
        <li v-for="(rate, currency) in rates" :key="currency">
          {{ currency }}: {{ rate }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import exchangeAPI from '../apis/exchangeAPI'

const amount = ref(1000)
const fromCurrency = ref('KRW')
const rates = ref(null)
const loading = ref(false)
const error = ref(null)

const fetchRates = async () => {
  loading.value = true
  error.value = null
  rates.value = null

  try {
    const response = await exchangeAPI.getRates(fromCurrency.value)
    rates.value = response
  } catch (err) {
    error.value = '환율 정보를 가져오는 데 실패했습니다.'
    console.error(err)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
form {
  max-width: 400px;
  margin: 20px auto;
}

div {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input, select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #2D60FF;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:disabled {
  background-color: #ccc;
}

.error {
  color: red;
  margin: 10px 0;
}

.results {
  margin-top: 20px;
}

.results ul {
  list-style: none;
  padding: 0;
}

.results li {
  padding: 5px 0;
}
</style>
