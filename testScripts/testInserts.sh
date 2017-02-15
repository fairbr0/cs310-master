curl --data "title=Article&author=Jake&content=Testarticle&source=BBC&url=google" http://localhost:6200/process -u jake:python
curl --data "title=Article&author=Jake&content=Testarticle&source=BBC&url=google" http://localhost:6200/process -u jake:python
curl --data "title=Article&author=Jake&content=Testarticle&source=The%20Guardian&url=google" http://localhost:6200/process -u jake:python
curl --data "title=Article&author=Jake&content=Testarticle&source=CNN&url=google" http://localhost:6200/process -u jake:python

