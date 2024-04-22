import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  vus: 10, // số lượng người dùng ảo
  duration: '12s', // thời gian chạy kiểm thử
};

const wordData = "các quy định mức điểm học phần các phương tiện bền vững công việc đánh giá".split(" ");

export default function () {
  // Chuẩn bị dữ liệu cho yêu cầu POST
  const data = {
    current_frequence: wordData[Math.floor(Math.random() * wordData.length)], // Chọn ngẫu nhiên một từ trong wordData
    next_words: 2, // số từ tiếp theo muốn dự đoán
    num_samples: 2 // số lượng mẫu dự đoán
  };

  // Gửi yêu cầu POST đến API
  const res = http.post('http://192.168.88.60:5555/words_rs_biLSTM', JSON.stringify(data), {
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
