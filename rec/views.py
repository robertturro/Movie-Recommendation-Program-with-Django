from django.shortcuts import render
from django.http import JsonResponse
import pickle
from .models import Recommendation



def rec(request):
	return render(request, 'rec.html')

def rec_movie(request):
	with open('md.pkl', 'rb') as handle:
		md = pickle.load(handle)

	clicked = 0

	if request.POST.get('action') == 'post':
		release_year = float(request.POST.get('release_year'))
		movie_input = str(request.POST.get('movie_input'))

	movie_found = False

	movs = []
	for key,value in md['movie_title'].items():
		if md['movie_title'][key] == movie_input:
			movs.append(key)
			movie_found = True

	movs2=[]
	for i in range(len(movs)):
		if md['year_released'][movs[i]] == release_year:
			movs2.append(movs[i])

	if len(movs2) == 0:
		movie_found = False

	if len(movs2) > 0:

		index = movs2[0]
		gen = md['genres'][index]
		ol = md['original_language'][index]

		ids = []
		for key,value in md['genres'].items():
			if md['genres'][key] == gen:
				ids.append(key)

		lst2 = []
		if release_year >= 2000:
			for i in range(len(ids)):
				if md['year_released'][ids[i]] >= 2000:
					lst2.append(ids[i])
		if (release_year < 2000) and (release_year >= 1970):
			for j in range(len(ids)):
				if (md['year_released'][ids[j]] < 2000) and (md['year_released'][ids[j]] >= 1970):
					lst2.append(ids[j])
		if release_year < 1970:
			for k in range(len(ids)):
				if (md['year_released'][ids[k]] < 1970):
					lst2.append(ids[k])

		lst3 = []
		for i in range(len(lst2)):
			if md['original_language'][lst2[i]] == ol:
				lst3.append(lst2[i])

		pop_d = {}
		for i in range(len(lst3)):
			pop_d[lst3[i]] = md['popularity'][lst3[i]]

		new_d = dict(sorted(pop_d.items(), key=lambda item: item[1], reverse=True))
		res = list(new_d.keys())

		for i in range(len(res)):
			if md['movie_title'][res[i]] == movie_input:
				continue
			else:
				result = md['movie_title'][res[i]]
				overview = md['overview'][res[i]]
				break


	if movie_found == False:
		result = "Movie Not Found. Make Sure Spelling And Release Date Are Correct"
		overview = "None"

	Recommendation.objects.create(movie_input=movie_input, release_year=release_year, result=result, overview=overview)

	return JsonResponse({'result':result,'movie_input':movie_input,'release_year':release_year,'overview':overview})


def view_results(request):
	data = {"dataset": Recommendation.objects.all()}
	return render(request, "results.html", data)

