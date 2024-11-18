<template>
  <div class="article-detail">
    <h1>게시글 상세 페이지</h1>
    <p>게시글 ID: {{ articleId }}</p>
    <!-- 여기에서 articleId를 사용하여 게시글 데이터를 가져오세요 -->
  </div>
</template>

<script>
import articlesAPI from '../apis/articlesAPI'

export default {
  name: 'ArticleDetailView',
  props: {
    articleId: {
      type: String,
      required: true
    }
  },
  mounted() {
    this.fetchArticle(this.articleId)
  },
  data() {
    return {
      article: null,
      loading: false,
      error: null
    }
  },
  methods: {
    async fetchArticle(id) {
      try {
        this.loading = true
        this.article = await articlesAPI.getArticle(id)
      } catch (error) {
        this.error = '게시글을 불러오는 데 실패했습니다.'
        console.error('게시글 로딩 에러:', error)
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
/* 스타일 추가 */
</style>
