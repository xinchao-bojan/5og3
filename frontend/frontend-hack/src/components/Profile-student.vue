<template>
  <div class="container">
    <div class="profile-wrapper">
      <div class="profile-card col-4">
        <div class="profile__name profile-item">
          <span class="profile__attr"
            >{{ user.firstname }} {{ user.lastname }}</span
          >
        </div>
        <br />
        <hr />
        <br />
        <div class="profile__sex profile-item">
          <span class="profile__attr">Пол: </span>
          <span>{{ user.sex }}</span>
        </div>
        <div class="profile__age profile-item">
          <span class="profile__attr">Возраст: </span>
          <span>23 года</span>
        </div>
        <div class="profile__institut profile-item">
          <span class="profile__attr">Вуз: </span>
          <span>{{ user.university }}</span>
        </div>
        <div class="profile__route profile-item">
          <span class="profile__attr">Направление: </span>
          <span>{{ user.direction }}</span>
        </div>
      </div>
      <div class="profile-change col-8">
        <div class="btn-div">
          <router-link to="/ChangeStudentCard">
            <button class="btn-change">Редактировать профиль</button>
          </router-link>
        </div>
        <div class="profile-compet">
          <h3 style="margin-bottom: 30px">Компетенции</h3>
          <div class="list-compet">
            <li class="__item" v-for="item in user.comps" :key="item">
              {{ item }}
            </li>
          </div>
        </div>
      </div>
    </div>
    <br />
    <hr />
    <br />
    <br />
    <div class="internships">
      <h2>Предлагаемые стажировки</h2>
      <div class="proposed">
        <div class="__item">
          <div class="col-4 descr">
            <h4>ОАО Роснефть</h4>
            <p class="prof">Профессия: VR/AR разработчик</p>
            <span
              >Разработка обучающего ПО в виртуальной реальности для
              обучения.</span
            >
          </div>
          <div class="col-4 skills">
            <h4>Требуемые навыки</h4>
            <div class="list-compet">
              <li class="__item">Разработка мобильных приложений</li>
              <li class="__item">Дизайн Интерфейсов</li>
              <li class="__item">VR разработка</li>
            </div>
          </div>
          <div class="col-4 period">
            <h4>Срок стажировки</h4>
            <span> От 3 до 6 месяцев</span>
            <div class="btns">
              <button class="butt-success">Принять</button>
              <button class="butt-ignore">Отказаться</button>
            </div>
          </div>
        </div>
        <div class="__item">
          <div class="col-4 descr">
            <h4>ОАО Роснефть</h4>
            <p class="prof">Профессия: VR/AR разработчик</p>
            <span
              >Разработка обучающего ПО в виртуальной реальности для
              обучения.</span
            >
          </div>
          <div class="col-4 skills">
            <h4>Требуемые Компетенции</h4>
            <div class="list-compet">
              <li class="__item">Разработка мобильных приложений</li>
              <li class="__item">Дизайн Интерфейсов</li>
              <li class="__item">VR разработка</li>
            </div>
          </div>
          <div class="col-4 period">
            <h4>Срок стажировки</h4>
            <span> От 3 до 6 месяцев</span>
            <div class="btns">
              <button class="butt-success">Принять</button>
              <button class="butt-ignore">Отказаться</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapActions, mapGetters } from "vuex";

export default {
  setup() {},
  data() {
    return {
      user: {
        firstname: "Константин",
        lastname: "Суроегин",
        sex: "Мужской",
        university: "РТУ МИРЭА",
        dateBorn: "2021-01-02",
        direction: "Программная инженерия",
        comps: [
          "Разработка мобильных приложений",
          "Дизайн Интерфейсов",
          "Разработка веб-сайтов",
          "VR разработка",
        ],
      },
    };
  },
  methods: {
    ...mapActions(["GET_EMPLOYERS_FROM_API"]),
  },
  computed: {
    ...mapGetters(["EMPLOYERS"]),
  },
  mounted() {
    console.log("hello from mounted ARTICLES: ");
    this.GET_EMPLOYERS_FROM_API();
  },
};
</script>
<style lang="scss">
.profile-wrapper {
  margin-top: 100px;
  display: flex;
  flex-direction: row;
  margin-bottom: 30px;
}
.profile-change {
  margin-left: 15px;
}
.profile-card {
  border: 1px solid black;
  border-radius: 10px;
  padding: 10px 10px 50px 10px;
  max-width: 370px;
  .profile__name {
    font-weight: bold;
    font-size: 18px;
    line-height: 22px;
  }
  .profile-item {
    display: flex;
    justify-content: space-between;
  }
}
.profile__attr {
  font-weight: bold;
}

.btn-change {
  background-color: #1319ad;
  color: #fff;
  font-size: 15px;
  line-height: 22px;
  border-radius: 50px;
  padding: 10px 20px;
}
.profile-compet {
  text-align: left;
}
.btn-div {
  text-align: right;
}
.list-compet {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  .__item {
    background-color: #e8e8f7;
    border: 1px solid black;
    border-radius: 50px;
    margin-right: 15px;
    margin-bottom: 15px;
    padding: 3px 14px;
  }
}

.internships {
  h2 {
    margin-bottom: 40px;
  }
  .proposed {
    .__item {
      display: flex;
      border: 1px solid black;
      border-radius: 10px;
      margin-bottom: 25px;
      .descr {
        h4 {
          color: #1319ad;
        }
        .prof {
          font-weight: bold;
        }
      }
      h4 {
        margin-bottom: 20px;
      }
      .period {
        .butt-success {
          background-color: transparent;
          color: #06a53c;
          border: 1px solid #06a53c;
          border-radius: 50px;
          padding: 5px 20px;
          margin-right: 10px;
        }
        .butt-ignore {
          color: #bf1a42;
        }
        .btns {
          margin-top: 20px;
        }
      }
    }
  }
}
</style>