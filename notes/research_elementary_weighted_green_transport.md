# Sharp weighted estimates for two original boundary equations

Research note, 3 November 2026.

The primitive upper bidiagonal coordinate and the first even crossing
denominator have exponentially large inverses in the ordinary Euclidean
norm. Their natural factorial weights remove that growth exactly. In
those weighted norms both equations become finite first-difference
equations, with inverse norm asymptotic to \(2N/\pi\). This gives an
estimate for every forcing vector, including an error in a boundary
source. The weights themselves are essential: they cannot be omitted
when this equation is joined to another tangle.

## 1. The original equations and the weights

Let \(N\ge2\), \(D=N-1\), \(q=e^{\pi i/N}\), and \(Q=q^2\).
Use the original coordinates of the
[primitive cap calculation](research_quantum_cap_primitive_source.md)
and the [crossing-run continuants](research_crossing_run_quantum_continuants.md).
The two matrices considered here are
\[
 B_{jj}=-qQ^j,\qquad B_{j,j+1}=1-Q^{j+1},
 \tag{1}
\]
and
\[
 P_{jj}=Q^{-j},\qquad P_{j,j-1}=-q\,4\sin^2(j\pi/N).
 \tag{2}
\]
All unspecified entries are zero. Thus \(B\) is the primitive coordinate,
and \(P=P_1=qZ-q^2X\) is the first even denominator. Neither matrix
has a wrap entry. Put
\[
 S_j=\prod_{r=1}^j2\sin(r\pi/N),\qquad S_0=1,
 \tag{3}
\]
and define two norms on \(\mathbb C^N\):
\[
 \|v\|_B^2=\sum_{j=0}^D S_j^2|v_j|^2,
 \qquad
 \|v\|_P^2=\sum_{j=0}^D S_j^{-4}|v_j|^2.
 \tag{4}
\]
Every weight is finite and strictly positive, at both level parities.

**Theorem 1.** The exact induced inverse norms are
\[
 \boxed{\quad
 \|B^{-1}\|_{B\to B}=\|P^{-1}\|_{P\to P}
     =\frac1{2\sin(\pi/(4N+2))}.
 \quad} \tag{5}
\]
In particular an error \(r\) in either equation changes its solution by
at most the right-hand side of (5) times the norm of \(r\), in the
corresponding weighted norm. The constant is \(2N/\pi+O(1)\).

*Proof.* Let \(T\) be the strictly upper shift, \(T_{j,j+1}=1\).
For \((Q;Q)_j=\prod_{r=1}^j(1-Q^r)\), set
\[
 g_j=\frac{q^{j^2}}{(Q;Q)_j},\qquad
 h_j=q^{j(j+2)}S_j^2.
 \tag{6}
\]
Their consecutive ratios give the exact diagonal conjugations
\[
 \begin{split}
 \operatorname{diag}(g)^{-1}B\operatorname{diag}(g)
       &=\operatorname{diag}(-qQ^j)(I-T),\\
 \operatorname{diag}(h)^{-1}P\operatorname{diag}(h)
       &=\operatorname{diag}(Q^{-j})(I-T^T).
 \end{split} \tag{7}
\]
For example,
\((1-Q^{j+1})g_{j+1}/g_j=qQ^j\), the negative of the
diagonal entry in (1). The lower off-diagonal calculation uses
\(h_j/h_{j-1}=q^{2j+1}4\sin^2(j\pi/N)\).
The endpoint rows in (7) remain present.

The two diagonal factors on the right are unitary. Since
\(|g_j|=S_j^{-1}\) and \(|h_j|=S_j^2\), the conjugations on
the left identify the norms (4) with the Euclidean norm. It remains
to compute \(\|(I-T)^{-1}\|_2\); transposition has the same norm.

The matrix \((I-T)^*(I-T)\) has first diagonal entry one, all other
diagonal entries two, and off-diagonal entries minus one. Its
eigenvectors have components \(\cos((j+1/2)\theta)\). The first
row is equivalent to the condition \(v_{-1}=v_0\), and the last
to \(v_N=0\). Thus its eigenvalues are
\[
 4\sin^2\!\left(\frac{(2k-1)\pi}{4N+2}\right),
       \qquad 1\le k\le N.
 \tag{8}
\]
These are distinct and give all \(N\) eigenvalues. The smallest
one proves (5). \(\square\)

The pointwise forms, which retain where the forcing occurs, are
\[
 \begin{split}
 |(B^{-1}f)_j|&\le S_j^{-1}\sum_{k=j}^D S_k|f_k|,\\
 |(P^{-1}f)_j|&\le S_j^2\sum_{k=0}^j S_k^{-2}|f_k|.
 \end{split} \tag{9}
\]
They follow from \((I-T)^{-1}=I+T+\cdots+T^D\) and its
transpose. No cancellation assumption is used in these upper bounds.

## 2. What the weights cost in the ordinary norm

Write
\[
 J(x)=\int_0^x\log(2\sin\pi t)\,dt,\quad 0\le x\le1,
 \qquad a=-J(1/6)>0.
 \tag{10}
\]
The integral is improper only at its endpoints. It is finite there,
and \(J(1)=0\). In fact \(J(1-x)=-J(x)\), and
\(J'(x)=\log(2\sin\pi x)\) changes sign only at \(1/6,5/6\).
Consequently \(\min J=-a\) and \(\max J=a\).

**Lemma 2.** Uniformly for \(0\le j<N\),
\[
                   \log S_j=NJ(j/N)+O(\log N).       \tag{11}
\]

*Proof.* On \([0,1/2]\), the function
\(\log(2\sin\pi t)\) is increasing. Comparing each sample with
the integrals on its two neighboring mesh intervals bounds the
error of its partial right sum by \(O(\log N)\), uniformly in the
partial endpoint. The first interval contributes
\(N\int_0^{1/N}\log(2\sin\pi t)\,dt=-\log N+O(1)\).
This also treats that interval explicitly instead of sampling its
singular endpoint. The analogous decreasing comparison on
\([1/2,1-1/N]\) has endpoint size \(O(\log N)\).
Splitting a partial sum at \(\lfloor N/2\rfloor\), with at most
one remaining mesh interval, proves (11).

For completeness, \(J(1)=0\) follows from the elementary double-angle
integral for \(\log\sin\), and reflection of its integrand gives
\(J(1-x)=-J(x)\). These identities involve convergent improper
integrals. \(\square\)

**Corollary 3.** In the unweighted Euclidean norm,
\[
 \begin{split}
 \lim_{N\to\infty}N^{-1}\log\|B^{-1}\|_2&=2a,\\
 \lim_{N\to\infty}N^{-1}\log\|P^{-1}\|_2&=4a,\\
 \lim_{N\to\infty}N^{-1}\log\|B^{-1}\mathbf e_D\|_2&=a,\\
 \lim_{N\to\infty}N^{-1}\log\|P^{-1}\mathbf e_0\|_2&=2a.
 \end{split} \tag{12}
\]

*Proof.* Formula (7) gives, with no error,
\[
 |(B^{-1})_{jk}|=S_k/S_j\quad(j\le k),\qquad
 |(P^{-1})_{jk}|=S_j^2/S_k^2\quad(k\le j).
 \tag{13}
\]
By (11), the limiting largest-entry exponents are respectively
\(\max_{x\le y}(J(y)-J(x))=2a\) and twice that value. The
ordered maximum is attained at \(x=1/6,y=5/6\). The spectral norm
lies between the largest entry and \(N\) times that entry, giving
the first two limits. For the last column of \(B^{-1}\), use
\(S_D=N\), which follows by differentiating \(z^N-1\) at one
and taking absolute values. Its maximal rate is \(-\min J=a\).
For the first column of \(P^{-1}\), the maximal rate is
\(2\max J=2a\). A column norm differs from its largest entry by
at most \(\sqrt N\). This proves the remaining limits. \(\square\)

## 3. Consequence for the retained boundary source

The original two-crossing vector satisfies
\(Bf_{JM^2}=(-1)^D\mathbf e_D\). Thus Theorem 1 gives a
polynomial error bound when the forcing is measured with exactly
the factorial weights in (4). Corollary 3 distinguishes the
exponential rate of this particular forcing from the larger norm
of the whole inverse. Its final component nevertheless has absolute
value one, as proved in the primitive cap note. A large interior
solution does not imply a large closing scalar.

For a general word the next turn or crossing changes the equation
and its natural weight. Applying (5) successively would require
estimating those changes of weight and the final boundary
evaluation. Their exponential cost is not covered by (5). In
particular these elementary estimates do not prove that the
geometric contribution survives in a connected short-filled region.
They supply a precise form of boundary-to-interior error transport
for two actual equations, with its full exponential weight retained.

The [matrix diagnostic](../experiments/check_elementary_weighted_green_transport.py)
checks the gauges against the original Newton multiplication matrix,
the forced endpoint rows, and the exact weighted singular values.
Its [saved output](../repro/results/research-elementary-weighted-green-transport.json)
contains 19 levels of both parities and 6,618 inverse entries at
120 decimal digits. The all-level estimates are proved above.
