$(document).ready(function () {
  set_temp();
  listing();
  get_star();
  GetCardBox();
});

function set_temp() {
  $.ajax({
    type: "GET",
    url: "http://spartacodingclub.shop/sparta_api/weather/chuncheon",
    data: {},
    success: function (response) {
      $("#temp").text(response["temp"]);

      let url = response["icon"];
      $("#weather").attr("src", url);
    },
  });
}

function posting() {
  let num = event.target.parentElement.lastElementChild.id[10];
  console.log(num);
  let opinion = $(`#opinion_${num}`).val();
  let star = $(`#star_${num}`).val();
  $.ajax({
    type: "POST",
    url: "/reviews",
    data: {
      opinion_value: opinion,
      star_value: star,
      num_value: num,
    },
    success: function (response) {
      alert(response["msg"]);
      window.location.reload();
    },
  });
}

function listing() {
  $.ajax({
    type: "GET",
    url: "/reviews",
    data: {},
    success: function (response) {
      let rows = response["reviews"];
      for (let i = 0; i < rows.length; i++) {
        let review = rows[i]["opinion"];
        let star = rows[i]["star"];
        let idnum = rows[i]["num"];
        let star_img = "⭐".repeat(star);

        let temp_html = `<p><a>${star_img}</a>
                            <a>${review}</a><p/>`;
        $(`#reviewbox_${idnum}`).append(temp_html);
      }
    },
  });
}

function get_star() {
  // 카드박스마다 점수와 별을 붙여주는 함수
  let sumScore_1 = 0;
  let count_1 = 0;
  let sumScore_2 = 0;
  let count_2 = 0;
  let sumScore_3 = 0;
  let count_3 = 0;
  let sumScore_4 = 0;
  let count_4 = 0;
  let sumScore_5 = 0;
  let count_5 = 0;
  let sumScore_6 = 0;
  let count_6 = 0;

  $.ajax({
    type: "GET",
    url: "/reviews",
    data: {},
    success: function (response) {
      let rows = response["reviews"];
      for (let i = 0; i < rows.length; i++) {
        let star = rows[i]["star"];
        let idnum = rows[i]["num"];
        if (idnum == 1) {
          sumScore_1 += Number(star);
          count_1 += 1;
          console.log(sumScore_1);
        } else if (idnum == 2) {
          sumScore_2 += Number(star);
          count_2 += 1;
        } else if (idnum == 3) {
          sumScore_3 += Number(star);
          count_3 += 1;
        } else if (idnum == 4) {
          sumScore_4 += Number(star);
          count_4 += 1;
        } else if (idnum == 5) {
          sumScore_5 += Number(star);
          count_5 += 1;
        } else if (idnum == 6) {
          sumScore_6 += Number(star);
          count_6 += 1;
        }
      }

      let score_1 = sumScore_1 / count_1;
      let getScore_1 = parseFloat(score_1).toFixed(2);
      let star_img_1 = "⭐".repeat(getScore_1);
      let temp_star_1 = `<a>${star_img_1} ${getScore_1}</a>`;
      $(`#score_1`).append(temp_star_1);

      let score_2 = sumScore_2 / count_2;
      let getScore_2 = parseFloat(score_2).toFixed(2);
      let star_img_2 = "⭐".repeat(getScore_2);
      let temp_star_2 = `<a>${star_img_2} ${getScore_2}</a>`;
      $(`#score_2`).append(temp_star_2);

      let score_3 = sumScore_3 / count_3;
      let getScore_3 = parseFloat(score_3).toFixed(2);
      let star_img_3 = "⭐".repeat(getScore_3);
      let temp_star_3 = `<a>${star_img_3} ${getScore_3}</a>`;
      $(`#score_3`).append(temp_star_3);

      let score_4 = sumScore_4 / count_4;
      let getScore_4 = parseFloat(score_4).toFixed(2);
      let star_img_4 = "⭐".repeat(getScore_4);
      let temp_star_4 = `<a>${star_img_4} ${getScore_4}</a>`;
      $(`#score_4`).append(temp_star_4);

      let score_5 = sumScore_5 / count_5;
      let getScore_5 = parseFloat(score_5).toFixed(2);
      let star_img_5 = "⭐".repeat(getScore_5);
      let temp_star_5 = `<a>${star_img_5} ${getScore_5}</a>`;
      $(`#score_5`).append(temp_star_5);

      let score_6 = sumScore_6 / count_6;
      let getScore_6 = parseFloat(score_6).toFixed(2);
      let star_img_6 = "⭐".repeat(getScore_6);
      let temp_star_6 = `<a>${star_img_6} ${getScore_6}</a>`;
      $(`#score_6`).append(temp_star_6);
    },
  });
  sumScore_1 = 0;
  count_1 = 0;
  sumScore_2 = 0;
  count_2 = 0;
  sumScore_3 = 0;
  count_3 = 0;
  sumScore_4 = 0;
  count_4 = 0;
  sumScore_5 = 0;
  count_5 = 0;
  sumScore_6 = 0;
  count_6 = 0;
}

function GetCardBox() {
  let countnum = 2;
  $.ajax({
    type: "GET",
    url: "/GetCardBox",
    data: {},
    success: function (response) {
      console.log(response);
      for (let i = 0; i < rows.length; i++) {
        let img = rows[i]["img"];
        let subs = rows[i]["subs"];
        let name = rows[i]["name"];

        let temp_html = `<div class="col">
                            <div class="card">
                              <img
                                src="${img}"
                                class="card-img-top"
                                alt="..."
                              />
                              <div class="card-body">
                                <h5 class="card-title">
                                  ${name} <a id="score_${countnum}">평균점수</a>
                                </h5>
                                <p class="card-text">
                                  ${subs}
                                </p>
                                <select
                                  class="form-select"
                                  aria-label="Default select example"
                                  id="star_${countnum}"
                                >
                                  <option selected>별점을 선택해주세요.</option>
                                  <option value="1">⭐</option>
                                  <option value="2">⭐⭐</option>
                                  <option value="3">⭐⭐⭐</option>
                                  <option value="4">⭐⭐⭐⭐</option>
                                  <option value="5">⭐⭐⭐⭐⭐</option>
                                </select>
                                <input id="opinion_${countnum}" />
                                <button type="button" class="btn btn-light" onclick="posting()">
                                  입력
                                </button>
                                <div class="review" id="reviewbox_${countnum}"></div>
                              </div>
                            </div>
                          </div>`;
        $(`#cards-box`).append(temp_html);
        countnum += 1;
      }
      countnum = 2;
    },
  });
}
