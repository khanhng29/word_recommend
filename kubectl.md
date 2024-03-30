# Tương Tác với Kubernetes

## Giới Thiệu

Repository này mô tả cách tương tác với một môi trường Kubernetes để quản lý triển khai (deployment), dịch vụ (service), và các tài nguyên khác thông qua sử dụng các lệnh cơ bản của kubectl.

## Cách Sử Dụng

### 1. Áp dụng tệp Manifest triển khai Kubernetes

Để áp dụng cấu hình từ một tệp YAML manifest, sử dụng lệnh `kubectl apply`. Ví dụ:

```bash
kubectl apply -f <path-to-manifest-file>
```

Ex:

```bash
kubectl apply -f .\recommender-manifest.yaml
```

### 2. Xem danh sách các triển khai và Dịch vụ

Để xem danh sách các triển khai và dịch vụ hiện có trong cụm Kubernetes, sử dụng lệnh `kubectl get`. Ví dụ:

```bash
kubectl get deployments
kubectl get services
```

### 3. Kiểm tra trạng thái của Pod và Triển khai

Để kiểm tra trạng thái của các pod và triển khai, sử dụng lệnh `kubectl describe`. Ví dụ:

```bash
kubectl describe pods <pod-name>
kubectl describe deployment <deployment-name>
```

### 4 .Giảm hoặc Tăng Quy Mô Triển Khai

- Để giảm hoặc tăng số lượng bản sao của một triển khai, sử dụng lệnh `kubectl scale`. Ví dụ:

```bash
kubectl scale deployment <deployment-name> --replicas=<desired-replica-count>
```

Ex: Giảm quy mô

```bash
kubectl scale deployment recommender-deployment --replicas=0
```

Ex: Tăng quy mô

```bash
kubectl scale deployment recommender-deployment --replicas=3
```

### 5. Xóa tất cả các Pod

```bash
kubectl delete pods --all --all-namespaces
```

### 6. Dừng và Xóa Container Docker

```bash
docker stop $(docker ps -aq)  # Dừng tất cả các container đang chạy
docker rm $(docker ps -aq)    # Xóa tất cả các container đã dừng
```

### 7. Xóa tất cả các triển khai Kubernetes

```bash
kubectl delete deployment --all  # Xóa tất cả các triển khai
```

**Note:**
Nếu cần xóa tất cả các triển khai và các tài nguyên khác như dịch vụ, tài nguyên phiên bản, v.v., có thể sử dụng lệnh tương ứng của Kubernetes:

```bash
kubectl delete all --all          # Xóa tất cả các tài nguyên trong cụm Kubernetes
```

Lưu ý rằng việc xóa tất cả các triển khai và tài nguyên trong cụm Kubernetes có thể gây mất mát dữ liệu không mong muốn, vì vậy hãy sử dụng cẩn thận và chắc chắn rằng đã sao lưu và xác nhận trước khi thực hiện.

## Create [Kubernet Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)

### 1. Triển Khai và Truy Cập vào Kubernetes Dashboard

Để triển khai và truy cập vào Kubernetes Dashboard, hãy sử dụng các bước sau:

**a. Triển khai Kubernetes Dashboard:**

- Lấy version mới tại trang [Kubernet Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.3.1/aio/deploy/recommended.yaml
```

**b. Tạo một Service Account và ClusterRoleBinding cho Dashboard:**

```bash
kubectl create serviceaccount dashboard-admin-sa
kubectl create clusterrolebinding dashboard-admin-sa --clusterrole=cluster-admin --serviceaccount=default:dashboard-admin-sa
```

**c. Lấy token để đăng nhập vào Dashboard:**

```bash
kubectl -n kubernetes-dashboard create token admin-user
```

**d. Bắt đầu proxy để truy cập vào Dashboard:**

```bash
kubectl proxy
```

**e. Mở trình duyệt và truy cập vào URL sau:**

```bash
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
```

**f. Chọn "Token" và dán token bạn đã sao chép trước đó, sau đó nhấp "Sign in".**

## Tài liệu tham khảo

- [Kubectl Overview](https://jamesdefabia.github.io/docs/user-guide/kubectl-overview/)
- [Kubernet Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)
