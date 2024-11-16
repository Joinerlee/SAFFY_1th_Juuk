import axios from 'axios'

const DEFAULT_RATES = {
    'USD': 0.00075,
    'EUR': 0.00070,
    'JPY': 0.11,
    'KRW': 1.0
}

class ExchangeAPI {
    constructor() {
        this.client = axios.create({
            baseURL: 'https://api.exchangerate-api.com/v4',
            timeout: 5000
        })
    }

    async getRates(baseCurrency = 'KRW') {
        try {
            // API 요청이 실패하더라도 테스트용 데이터를 반환하기 위해
            // 기본 환율에서 동적으로 계산
            const baseRate = DEFAULT_RATES[baseCurrency] || 1
            
            const mockRates = Object.entries(DEFAULT_RATES).reduce((acc, [currency, rate]) => {
                if (currency === baseCurrency) {
                    acc[currency] = 1
                } else {
                    acc[currency] = rate / DEFAULT_RATES[baseCurrency]
                }
                return acc
            }, {})

            // 실제 API 호출 (주석 처리)
            // const response = await this.client.get(`/latest/${baseCurrency}`)
            // return response.data.rates

            // 테스트용 지연 추가
            await new Promise(resolve => setTimeout(resolve, 800))
            
            return mockRates
        } catch (error) {
            console.error('환율 정보 조회 실패:', error)
            throw new Error('환율 정보를 불러오는데 실패했습니다.')
        }
    }

    async convert(amount, fromCurrency = 'KRW', toCurrency = 'USD') {
        try {
            const rates = await this.getRates(fromCurrency)
            const convertedAmount = amount * rates[toCurrency]
            
            return {
                amount: Math.round(convertedAmount * 100) / 100,
                from: fromCurrency,
                to: toCurrency
            }
        } catch (error) {
            console.error('환율 변환 실패:', error)
            throw error
        }
    }
}

export default new ExchangeAPI()