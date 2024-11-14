<template>
    <nav class="navigation-bar">
        <div class="nav-container">
            <div class="logo">
                <router-link to="/">JuukJuuk</router-link>
            </div>
            <div class="nav-links">
                <router-link to="/" class="nav-link">홈</router-link>
                <router-link to="/exchange" class="nav-link">환율 계산</router-link>
                <router-link to="/nearby-banks" class="nav-link">주변 은행</router-link>
                <router-link to="/community" class="nav-link">커뮤니티</router-link>
                <router-link to="/product-recommendation" class="nav-link">금융 상품 추천</router-link>
            </div>
        </div>
    </nav>
    <!-- 네비게이션 바 높이만큼 여백 추가 -->
    <div class="nav-spacer"></div>
</template>

<style scoped>
.navigation-bar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background-color: white;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    z-index: 1000;
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
    height: 56px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo a {
    color: #2D60FF;
    font-size: 1.25rem;
    font-weight: bold;
    text-decoration: none;
}

.nav-links {
    display: flex;
    gap: 24px;
}

.nav-link {
    color: #666;
    text-decoration: none;
    font-size: 0.95rem;
    padding: 8px 12px;
    position: relative;
    transition: color 0.2s;
}

.nav-link:hover {
    color: #2D60FF;
}

.nav-link.router-link-active {
    color: #2D60FF;
}

.nav-link.router-link-active::after {
    content: '';
    position: absolute;
    bottom: -17px;
    left: 0;
    width: 100%;
    height: 2px;
    background-color: #2D60FF;
}

.nav-spacer {
    height: 56px;
}

/* 모바일 반응형 */
@media (max-width: 768px) {
    .nav-container {
        padding: 0 10px;
    }
    
    .nav-links {
        gap: 10px;
    }
    
    .nav-link {
        font-size: 0.85rem;
        padding: 8px 6px;
    }
}
</style>