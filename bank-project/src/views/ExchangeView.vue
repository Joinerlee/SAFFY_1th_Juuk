<!-- Start of Selection -->
<!-- 환율 계산 페이지: Vue의 template은 HTML과 유사한 구조로, 사용자 인터페이스를 정의하는 데 사용됩니다. -->
<!-- 차이 : Vue는 가상DOM을 사용하여 조금더 동적으로 제어가 가능한 반면, 전통적인 html은 수동으로 DOM 요소를 조작해야 합니다. -->
<!-- 환율 계산: 이 컴포넌트는 환율 계산 기능을 제공하는 페이지입니다. -->

<!-- End of Selection -->
<template>
  <div class="exchange-view">
    <div class="card">
      <h1>환율 계산</h1>
    </div>
    <ExchangeCalculator />
  </div>
</template>

<style>
.card {
  background-color: #f9f9f9; /* 카드 배경색을 밝은 회색으로 변경 */
  border-radius: 8px; /* 모서리 둥글게 */
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); /* 그림자 효과를 더 부드럽게 */
  padding: 15px; /* 내부 여백을 줄임 */
  margin: 20px; /* 외부 여백 유지 */
  text-align: center; /* 텍스트 중앙 정렬 */
  border: 1px solid #e0e0e0; /* 얇은 테두리 추가 */
}
h1 {
  font-size: 1.8em; /* 글자 크기 조정 */
  color: #333; /* 글자 색상 조정 */
  margin: 0; /* 기본 여백 제거 */
}
</style>

<script>
import ExchangeCalculator from '../components/ExchangeCalculator.vue'

export default {
  name: 'ExchangeView',
  components: {
    ExchangeCalculator
  }
}
</script>