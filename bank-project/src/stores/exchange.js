// ====================
// 환율 계산 스토어 (Exchange Store)
// ====================
// pinia 라이브러리 사용 (Using Pinia Library)
// ====================
// 스토어란? (What is a Store?)
// 상태 관리를 위한 저장소 (A repository for state management)
// ====================

import { defineStore } from 'pinia'
import axios from 'axios'

// 환율 계산 스토어 정의
// defineStore 함수를 사용하여 스토어 생성
// Store의 기법 문법
// 1. state: 상태 정의
// 2. actions: 상태 변경 함수 정의
// 3. getters: 계산된 값 정의

export const useExchangeStore = defineStore('exchange', {
  state: () => ({
    rates: {},
    baseCurrency: 'USD',
    loading: false,
    error: null
  }),
  actions: {
    async fetchRates() {
      this.loading = true
      try {
        // 실제 애플리케이션에서는 환경 변수를 사용하여 API 키를 관리해야 합니다.
        const response = await axios.get(`https://openexchangerates.org/api/latest.json?app_id=YOUR_APP_ID`)
        this.rates = response.data.rates
        this.error = null
      } catch (error) {
        this.error = '환율 정보를 가져오는데 실패했습니다.'
        console.error('Error fetching exchange rates:', error)
      } finally {
        this.loading = false
      }
    }
  },
  getters: {
    availableCurrencies: (state) => Object.keys(state.rates)
  }
})