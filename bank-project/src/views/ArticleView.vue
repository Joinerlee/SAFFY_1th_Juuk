<!-- views/ArticleView -->
<template>
  <div>
    <h1>게시글 목록</h1>
    <ul>
      <li v-for="article in articles" :key="article.id">
        <router-link :to="`/articles/${article.id}`">{{ article.title }}</router-link>
      </li>
    </ul>
    <button @click="createArticle">새 게시글 작성</button>

    <!-- 게시글 생성 모달 (선택 사항) -->
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="showModal = false">&times;</span>
        <h2>새 게시글 작성</h2>
        <form @submit.prevent="submitArticle">
          <div>
            <label for="title">제목</label>
            <input id="title" v-model="newArticle.title" type="text" required />
          </div>
          <div>
            <label for="description">내용</label>
            <textarea id="description" v-model="newArticle.description" required></textarea>
          </div>
          <button type="submit">작성</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import articlesAPI from '../apis/articlesAPI';

export default {
  data() {
    return {
      articles: [],
      showModal: false,
      newArticle: {
        title: '',
        description: ''
      }
    };
  },
  async created() {
    try {
      this.articles = await articlesAPI.getArticles();
    } catch (error) {
      console.error('게시글 불러오기 실패:', error);
    }
  },
  methods: {
    createArticle() {
      this.showModal = true;
    },
    async submitArticle() {
      try {
        await articlesAPI.createArticle(this.newArticle);
        this.showModal = false;
        this.newArticle.title = '';
        this.newArticle.description = '';
        this.articles = await articlesAPI.getArticles(); // 게시글 목록 업데이트
      } catch (error) {
        console.error('게시글 작성 실패:', error);
      }
    }
  }
};
</script>

<style scoped>
/* 모달 스타일 */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  width: 400px;
}

.close {
  float: right;
  font-size: 1.5em;
  cursor: pointer;
}

form div {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input, textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  padding: 10px 15px;
  background-color: #2D60FF;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #1a45d1;
}
</style>