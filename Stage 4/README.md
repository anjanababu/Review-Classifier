# Review-Classifier
<b>Step 4 : Generating the Unigram Multinomial Naive Bayesian Model</b>
<ul>
<li>Trained a multinomial naive bayes model. </li>
<li>Used laplace smoothing/add one smoothing (to take care of the zero probabilities). </li>
<li>Saved the model making using of the <b>pickle</b> package.</li>
</ul>
The exported model file (<i>naiveBayesUnigramModel.p</i>), a human readable version of the model probabilities (<i>model.txt</i>) and the code used for training the model (<i>unigram_model.py</i>) are also included.</i>

<i>Note: the function 'trainingTheModel' ensures the reusability of the code for any training corpus</i>