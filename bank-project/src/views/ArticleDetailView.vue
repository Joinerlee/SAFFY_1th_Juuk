<template>
  <div class="article-detail">
    <h1>게시글 상세 페이지</h1>
    <p>게시글 ID: {{ articleId }}</p>
    <!-- 여기에서 articleId를 사용하여 게시글 데이터를 가져오세요 -->
  </div>
</template>

<script>
export default {
  name: 'ArticleDetailView',
  props: {
    articleId: {
      type: String,
      required: true
    }
  },
  mounted() {
    // 예: articleId를 사용하여 API에서 게시글 데이터 가져오기
    // this.fetchArticle(this.articleId)
  },
  methods: {
    fetchArticle(id) {
      // articlesAPI.getArticle(id).then(data => {
      //   // 데이터 처리
      // })
    }
  }
}
</script>
