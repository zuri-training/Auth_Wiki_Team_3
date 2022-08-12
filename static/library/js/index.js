// Dynamic Search Feature
const url = window.location.href;
const searchForm = document.getElementById("searchForm");
const search = document.getElementById("search");
const searchResultsBox = document.getElementById("search-results-box");
const csrf = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

sendSearchData = (query) => {
	const xhr = new XMLHttpRequest();
	const fd = new FormData();

	fd.append("csrfmiddlewaretoken", csrf);
	fd.append("query", query);

	xhr.open("post", "search/", true);

	xhr.onload = function () {
		if (xhr.status === 200) {
			const resObj = JSON.parse(xhr.responseText);
			console.log(resObj);
			const resArr = resObj.data;
			// searchResultsBox.innerHTML = res.data;

			if (Array.isArray(resArr)) {
				searchResultsBox.innerHTML = "";
				resArr.forEach((item) => {
					old_name = item.name;
					new_name = old_name.replaceAll(/ /gi, "-");
					console.log(new_name);
					searchResultsBox.innerHTML += `<a href="dashboard/${item.pk}" class="item">
          <section>
            <section class="image">${item.name[0]}</section>
            <section class="desc">
              <h3>${item.name}</h3>
              <p>${item.desc}</p>
            </section>
          </section>
          </a>`;
				});
			} else {
				if (search.value.length > 0) {
					searchResultsBox.innerHTML = `<h3>${resArr}</h3>`;
				}
			}
		}
	};

	xhr.onerror = function (error) {
		console.log(error);
	};

	xhr.send(fd);
};

search.addEventListener("input", (e) => {
	if (search.value.length > 0) {
		searchResultsBox.classList.remove("hide");
	} else {
		searchResultsBox.classList.add("hide");
	}

	sendSearchData(e.target.value);
});
