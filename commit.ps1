# 1. 변경 사항 스테이징
git add .

# 2. 새로 추가된(A) 파일들의 이름만 가져와서 확장자 제거 후 쉼표로 연결
$fileNames = git diff --cached --name-only --diff-filter=A | ForEach-Object { 
    [System.IO.Path]::GetFileNameWithoutExtension($_) 
}

# 배열을 ", "로 합치기
$commitMsg = $fileNames -join ", "

# 3. 파일 이름 존재 여부에 따른 조건부 커밋
if ([string]::IsNullOrWhiteSpace($commitMsg)) {
    Write-Host "새로운 파일이 없습니다. 기본 메시지로 커밋합니다." -ForegroundColor Cyan
    git commit -m "edit"
} else {
    git commit -m "$commitMsg"
    Write-Host "커밋 완료: $commitMsg" -ForegroundColor Green
}

# 4. 푸시
git push origin main