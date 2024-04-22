import http from 'k6/http';

export let options = {
  vus: 80, 
  duration: '120s',
};

const wordData = "các quy định mức điểm học phần các phương tiện bền vững công việc đánh giá".split(" ");

export default function () {
  const data = {
    current_frequence: wordData[Math.floor(Math.random() * wordData.length)], 
    next_words: 2,
    num_samples: 2
  };

  // Gửi yêu cầu POST đến API
  const res = http.post('http://192.168.88.64:5555/words_rs_biLSTM', JSON.stringify(data), {
    headers: {
      'Content-Type': 'application/json',
    },
  });

  // Kiểm tra xem yêu cầu có thành công không và in thông tin đáp ứng từ server
  if (res.status === 200) {
    console.log('Request successful. Response:', res.body);
  } else {
    console.error('Request failed. Status code:', res.status);
  }

  // Chờ một khoảng thời gian ngắn trước khi gửi yêu cầu tiếp theo
}
