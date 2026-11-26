# Why positivity of the crossing form does not give a uniform lower bound

Research proof, 3 November 2026. Frozen manuscripts are unchanged.

The [combined trace formula](research_trace_normal_defect_positive_form.md)
expresses the even-level crossing trace through a positive definite
matrix. That is useful: the first derivatives that previously appeared
as separate signed sums now belong to one positive form. But positive
definiteness at each finite level is weaker than a lower bound at the
exponential scale needed for the volume limit. Here that distinction is
necessary, not merely a precaution. For each fixed positive crossing
power the smallest eigenvalue is exponentially small as the level grows.

The proof constructs vectors supported at physical colors close to
\(-2\). Their first several weighted moments vanish. Analyticity of
the crossing kernel then makes their quadratic form small. The test
vectors can even have nonnegative entries. They are not the original
source vector. The result therefore
does not rule out a useful lower bound for that particular source.

## 1. The matrix and the claim

Let \(N\) be even, \(m=N/2\), and let \(n>0\) be fixed. Define
\[
 c_a=2\cos\frac{(2a+1)\pi}{N},\qquad
 \sigma_a=2(-1)^a\sin\frac{(2a+1)\pi}{N},\qquad
 \varphi(z)=\kappa f(z),\quad
 \kappa=\frac{nN}{4\pi},\quad f(z)=\arccos(-z/2)^2,
 \qquad 0\le a<m.
 \tag{1}
\]
The square in \(f\) is analytic at \(-2\), with \(f(-2)=0\)
and \(f'(-2)=1\). The positive crossing matrix \(H_{n,N}\)
of the combined trace formula has the exact entries
\[
 (H_{n,N})_{ab}=\sigma_a\sigma_b Q(c_a+2,c_b+2),\qquad
 Q(w,z)=\frac{1-\exp\{i\kappa[f(-2+z)-f(-2+w)]\}}{i(w-z)}.
 \tag{2}
\]
The diagonal of \(Q\) is defined by continuation. In particular,
\((H_{n,N})_{aa}=\sigma_a^2\kappa f'(c_a)>0\).

**Theorem.** Set
\[
 s=\max\{n,1\},\qquad \delta=\frac1{1024s}.
 \tag{3}
\]
For every even \(N\) with \(\delta N\ge4\),
\[
 0<\lambda_{\min}(H_{n,N})
       \le nN^2 e^{-\delta N}.
 \tag{4}
\]
There is a unit vector with nonnegative entries whose quadratic form
satisfies the upper bound in (4). Moreover
\(\|H_{n,N}\|\ge nN/8\). Consequently,
\[
 \frac{\lambda_{\min}(H_{n,N})}{\|H_{n,N}\|}
       \le 8N e^{-\delta N}.
 \tag{5}
\]
The constants are deliberately conservative. Their role is to show
an exponential obstruction for each fixed \(n\), not to estimate
the actual least eigenvalue sharply.

## 2. An analytic estimate near the complete color

Put \(g(w)=f(-2+w)\). The branch regular at zero satisfies
\[
 g(w)=4\arcsin(\sqrt w/2)^2.
 \tag{6}
\]
Although a square root appears on the right, the square of the odd
analytic function \(\arcsin\) makes the result analytic in \(w\)
for \(|w|<4\). For \(|w|\le r\le1\), differentiation gives
\[
 |g'(w)|
  =\left|\frac{\arcsin(\sqrt w/2)}
                 { (\sqrt w/2)\sqrt{1-w/4}}\right|
  \le\frac1{1-r/4}<2.
 \tag{7}
\]
To justify the inequality, write
\(\arcsin v/v=\int_0^1(1-t^2v^2)^{-1/2}\,dt\), with
its branch equal to one at zero. Both factors in (7) are bounded
by \((1-r/4)^{-1/2}\). Thus
\(|g(w)-g(z)|\le2|w-z|\) on this disk, and
\(|g(w)|\le2r\).

The elementary identity
\(e^{iv}-1=iv\int_0^1 e^{itv}\,dt\) gives
\(|e^{iv}-1|\le |v|e^{|\operatorname{Im}v|}\). Applying it
to (2) shows that \(Q\) is holomorphic on the bidisk and
\[
 |Q(w,z)|\le M:=2\kappa e^{4\kappa r}
                      \qquad (|w|,|z|\le r).
 \tag{8}
\]
If \(Q(w,z)=\sum_{i,j\ge0}q_{ij}w^iz^j\), the Cauchy
coefficient bound is therefore \(|q_{ij}|\le M r^{-i-j}\).

## 3. A vector whose low moments vanish

Take \(k=\lfloor\delta N\rfloor\) and use only the last \(k\)
physical nodes, namely \(m-k\le a<m\). They satisfy
\[
 0<c_a+2\le h:=4\pi^2\delta^2.
 \tag{9}
\]
Indeed their angular distances from \(\pi\) are at most
\(2\pi k/N\), and \(2(1-\cos v)\le v^2\).
There is a unit vector \(v\), supported on these nodes, such that
\[
 \mu_j:=\sum_a v_a\sigma_a(c_a+2)^j=0,
                        \qquad 0\le j\le k-2.
 \tag{10}
\]
These are \(k-1\) homogeneous linear equations in \(k\)
unknowns. For example, if \(w_a=c_a+2\), take a nonzero multiple
of \(1/(\sigma_a\prod_{b\ne a}(w_a-w_b))\) on this set,
then normalize it. The usual leading-coefficient formula for
polynomial interpolation proves (10). These entries have a common
sign: at position \(j\) in the decreasing list of selected nodes,
the product of differences has sign \((-1)^j\), while
\(\sigma_a\) has sign \((-1)^{m-k+j}\). Multiplying the
whole vector by \((-1)^{m-k}\) makes every entry positive on
its support.
For every remaining index, the Cauchy--Schwarz inequality and
\(|\sigma_a|\le2\) give
\[
                         |\mu_j|\le2\sqrt{k}\,h^j.
 \tag{11}
\]

Choose \(r=\delta/s\). This lies in \((0,1)\), and
\[
 q:=h/r=4\pi^2s\delta=\pi^2/256<1/16.
 \tag{12}
\]
The double Taylor series from (8) converges absolutely at every
selected node. In the quadratic form, (10) kills every term with
either index less than \(k-1\). Hence
\[
 0<v^*H_{n,N}v
  =\sum_{i,j\ge k-1}q_{ij}\overline{\mu_i}\mu_j
  \le\frac{4kM}{(1-q)^2}q^{2k-2}.
 \tag{13}
\]
Strict positivity here is the previously proved positive-form
theorem; the upper bound follows by taking absolute values only
after the moment cancellation.

Since \(\delta N\ge4\), we have \(2k-2\ge\delta N\).
Also \(4\kappa r\le\delta N/\pi\). The inequalities
\(\log16>2\) and \(1/\pi<1\) imply
\[
 e^{4\kappa r}q^{2k-2}\le e^{-\delta N}.
 \tag{14}
\]
Finally, using \(k\le N/2\) and \(\pi>3\),
\[
 \frac{8\kappa k}{(1-q)^2}
  \le\frac{nN^2}{\pi}\left(\frac{16}{15}\right)^2
  <nN^2.
 \tag{15}
\]
The variational characterization of the least eigenvalue proves
(4). A physical node with \(\tau=\arccos(-c_a/2)\) in
\([\pi/4,3\pi/4]\) exists for every even \(N\ge4\). At this
node the diagonal is
\(nN\tau\sin\tau/\pi\ge nN/8\). A positive matrix has norm
at least each diagonal entry, proving (5).

## 4. What a source lower bound would still require

There cannot be numbers \(\varepsilon_N\to0\) such that
\[
 F^*H_{n,N}F\ge e^{-\varepsilon_NN}\|F\|^2
 \tag{16}
\]
for every vector \(F\) and all large even levels: the vectors
constructed above violate such an inequality. The same obstruction
holds after normalizing by the operator norm, and even when (16)
is required only for vectors with nonnegative entries. Positivity
of the entries of a vector does not make the complex matrix entries
in its quadratic form nonnegative.

For the actual source, however, \(F_a=\mathcal L_N(c_a)\) is a
specified vector, not an arbitrary one. A lower bound could still
follow from its distribution among the spectral subspaces of
\(H_{n,N}\), or from a separate preparation estimate that excludes
the small-eigenvalue directions. The original knot closure also
retains its phased bilinear pairing, rather than the adjoint cap
that produces \(F^*H_{n,N}F\). Both requirements must be proved.

Thus the Fourier or representation-theoretic proposal has a precise
next task: establish an observation bound for the original source
and the original closing functional. Positive definiteness, or
almost-invariance without a quantitative spectral estimate and
control of that observation, does not supply it.

## 5. Reproduction

Run `python3 experiments/check_pick_form_small_eigenvalues.py`.
The script checks the rational constants and the moment cancellation
against the original finite crossing kernel. The proof of exponential decay is
the analytic estimate above, not an extrapolation of finite
eigenvalue calculations. The saved record is
[research-pick-form-small-eigenvalues.json](../repro/results/research-pick-form-small-eigenvalues.json).
