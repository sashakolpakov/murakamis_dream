# A uniform real-index reduction for mixed three/four cycles

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The fully contracted positive sine weights have a unique real entropy
maximum in one fixed compact box, for every cyclic word in three and
four. The full real-index complement has a uniform gap relative to
that maximum. This is an absolute-weight estimate. Its reference rate
is not the complex geometric critical action, and no coefficient lower
bound follows by discarding the quadratic oscillation.

## 1. The original polytope and entropy

Fix a cyclic word \(n_1,\ldots,n_m\in\{3,4\}\), \(m\ge1\),
and put \(\epsilon_v=1_{n_v=4}\), \(k=\sum_v\epsilon_v\).
Indices are cyclic. The exact original contraction has support
\[
 \mathcal P=\{(s_v,t_v):s_v,t_v\ge0,
                  \ s_v+t_v\le1,\ t_v+s_{v+1}\le1\}.
 \tag{1}
\]
Its entropy, including all sine-factorial denominators, is
\[
 H=\sum_v\{J(s_v+t_v)+J(t_v+s_{v+1})\}
       -\sum_v(2+\epsilon_v)\{J(s_v)+J(t_v)\},
 \quad J(z)=\int_0^z\log(2\sin\pi u)\,du.
 \tag{2}
\]
Use the continuous extension at zero and one. The primitive satisfies
\(J(0)=J(1/2)=J(1)=0\), \(J(1-z)=-J(z)\), and
\(J(z)>0\) on \(1/2<z<1\).
These follow directly from its derivative and its endpoint values.

Formula (2) is precisely the exponent of the absolute weights in
[the original contracted source](research_mixed_contracted_phase.md#1-an-exact-all-level-cyclic-source).
In particular it retains both vertex and shared-boundary support
conditions. We do not replace either family by an independent box
until a valid entropy comparison has been made.

## 2. Reflection into the half-cube

Define the tetrahedral entropy
\[
       V(x,y)=J(x+y)-J(x)-J(y),\qquad x,y\ge0,\quad x+y\le1.
 \tag{3}
\]
In the open triangle,
\[
 -V''=\pi\begin{pmatrix}
 \cot\pi x-\cot\pi(x+y)&-\cot\pi(x+y)\\
 -\cot\pi(x+y)&\cot\pi y-\cot\pi(x+y)
 \end{pmatrix},\qquad \det(-V'')=\pi^2.
 \tag{4}
\]
Its diagonal entries are positive, since, for example,
\(\cot\pi x-\cot\pi(x+y)=\sin\pi y/
[\sin\pi x\sin\pi(x+y)]\). Thus \(V\) is strictly concave.

View the legs as the vertices of the alternating cycle of original
vertex pairs and shared-boundary pairs; a two-leg cycle has two
incidences of the same pair. Then
\[
                  H=\sum_{\text{pairs}}V(x,y)
                         -\sum_{v:n_v=4}\{J(s_v)+J(t_v)\}.
 \tag{5}
\]
Every leg has two pair incidences, counted with multiplicity.

**Lemma 1.** Reflect each leg \(x>1/2\) to \(1-x\), leaving
the other legs unchanged. The resulting vector \(\widehat z\)
lies in \([0,1/2]^{2m}\), remains feasible, and
\(H(\widehat z)\ge H(z)\).

*Proof.* Two adjacent legs cannot both exceed \(1/2\). If
\(x>1/2\), either neighbor \(y\) satisfies \(0\le y\le1-x\),
so the reflected pair is feasible. Its entropy gain is
\[
 \Delta_x(y):=V(1-x,y)-V(x,y)
               =2J(x)-J(x-y)-J(x+y),
 \quad
 \Delta_x'(y)=\log\frac{\sin\pi(x-y)}{\sin\pi(x+y)}>0
 \tag{6}
\]
for \(0<y<1-x\), since \(\cos\pi x<0\).
Also \(\Delta_x(0)=0\); continuity handles the endpoints.
The extra type-four term gains \(2J(x)\ge0\).
All high legs are nonadjacent, so these comparisons may be added
without changing their neighbors. This proves the assertion. \(\square\)

On the half-cube every pair sum is at most one. The sum of its pair
entropies is strictly concave in the interior, and \(-J\) is concave
there because \(J''(x)=\pi\cot\pi x\ge0\) for \(x\le1/2\).
Consequently \(H\) is strictly concave in the interior half-cube,
with its continuous concave extension on the closed half-cube.

## 3. A fixed box containing the unique maximum

Put
\[
 l=13/50=.26,\quad h=39/100=.39,\qquad
 \mathcal B=[1/4,2/5]^{2m}.
 \tag{7}
\]
For a leg \(x\), write its two neighbors as \(y,z\), and let
\(\epsilon\) be the type of its original vertex. Its derivative is
\[
 H_x=\log\frac{4\sin\pi(x+y)\sin\pi(x+z)}
                       {(2\sin\pi x)^{2+\epsilon}}.
 \tag{8}
\]
On the lower face \(x=l\), with \(y,z\in[l,h]\), both pair sums
belong to \([.52,.65]\), so their sines are at least
\(\sin(13\pi/20)\). On the upper face \(x=h\), they belong to
\([.65,.78]\), and their sines are at most that same value.
The strict scalar inequalities
\[
 \begin{split}
 2\sin(13\pi/50)&>1,\qquad 2\sin(39\pi/100)>1,\\
 4\sin^2(13\pi/20)&>(2\sin(13\pi/50))^3,\\
 4\sin^2(13\pi/20)&<(2\sin(39\pi/100))^2
 \end{split}
 \tag{9}
\]
therefore make every lower-face derivative positive and every
upper-face derivative negative, for either type. These are explicit
one-dimensional outward comparisons, not a sample over the polytope.

**Theorem 2.** There is one global maximizer \(z_*\) of \(H\) on
\(\mathcal P\). It lies in \((l,h)^{2m}\). Write \(H_*=H(z_*)\).
For every \(z\in\mathcal P\setminus\mathcal B\),
\[
                         H(z)<H_*-\frac1{10000}.
 \tag{10}
\]
The box and the gap do not depend on the word or its length.

*Proof.* A maximum on \([l,h]^{2m}\) exists. The face derivative
signs force it into the interior, where its gradient vanishes.
Strict concavity makes it the unique maximum on the entire
half-cube. Lemma 1 proves that it is a global maximum on
\(\mathcal P\). If another maximum had a high leg, its reflected
vector would equal \(z_*\). That high leg would then have two
positive unchanged neighbors, so (6) would give a strict gain,
a contradiction. Thus the global maximum is unique.

On \(\mathcal B\), all pair sums are at least \(1/2\), and the
Hessian has the exact decomposition
\[
 -H''=\pi\operatorname{diag}((2+\epsilon_x)\cot\pi x)
      -\pi\sum_{\{x,y\}}\cot\pi(x+y)
                      (e_x+e_y)(e_x+e_y)^T
       \succeq 2\pi\cot(2\pi/5)I\succ2I.
 \tag{11}
\]
Let \(z\) be in the half-cube but outside \(\mathcal B\).
The ray from \(z_*\) first reaches its boundary at distance
strictly greater than \(1/100\). Integrating (11) up to this
first crossing gives loss greater than
\(\pi\cot(2\pi/5)/10000>1/10000\).
Concavity on the whole half-cube prevents any later increase along
the ray. This proves (10) in that case.

Now suppose \(z\) has a high leg, and reflect all high legs. If
\(\widehat z\notin\mathcal B\), apply the preceding result and
Lemma 1. There is one further case which cannot be omitted:
\(\widehat z\in\mathcal B\). Choose an original high leg.
Then \(x\in[3/5,3/4]\), and both its unchanged neighbors belong
to \([1/4,2/5]\). For \(0<y<1-x\),
\[
 \Delta_x''(y)=\frac{-\pi\sin(2\pi x)}
                    {\sin\pi(x-y)\sin\pi(x+y)}\ge\frac\pi2.
 \tag{12}
\]
Indeed \(-\sin(2\pi x)\ge\sin(\pi/5)>1/2\), and the
positive denominator is at most one. Since
\(\Delta_x(0)=\Delta_x'(0)=0\), each neighbor \(y\ge1/4\)
gives \(\Delta_x(y)\ge\pi/64\). The two incidences therefore
give total gain at least \(\pi/32>1/10000\). Endpoint cases
follow by continuity. Every other reflection contributes a
nonnegative gain. Hence (10) holds here as well. \(\square\)

## 4. The exact finite absolute-weight consequence

Use the original support \(\mathcal P_N\) and positive weights
\(W_N\) of the contracted source, so its literal cyclic scalar is
\[
 \kappa^{m+k}N^k\sum_{\mathcal P_N}W_N
       e^{iN\Theta+(i\pi/2)\sum_v\epsilon_v(s_v+t_v)}.
 \tag{13}
\]
The uniform sine-factorial estimate through both ends is
\(\log S_j=NJ(j/N)+O(\log N)\), \(0\le j<N\).
Thus each absolute summand, including the original \(N^k\), is
bounded by a polynomial times \(e^{NH}\). There are at most
\(N^{2m}\) summands. For any subset whose scaled indices are
outside \(\mathcal B\), Theorem 2 gives
\[
 \left|\kappa^{m+k}N^k\sum_{\text{subset}}W_Ne^{iN\Theta+\cdots}\right|
 \le C_mN^{q_m}\exp N(H_*-1/10000).
 \tag{14}
\]
The same bound holds for the sum of their absolute values. Fixed
\(O(N^{-1})\) changes of the cuts retain, for sufficiently large
\(N\), the weaker gap \(1/20000\). Constants and starting levels
may depend on the fixed word. No word length depending on \(N\)
is covered.

There is a useful precise profile of the entire absolute majorant.
Set
\[
 \mathcal A_N=N^k\sum_{\mathcal P_N}W_N,
 \quad L(z)=\sqrt{2\sin\pi z},\qquad
 a_0(z)=\frac{\prod_vL(s_v+t_v)L(t_v+s_{v+1})}
                {\prod_v\{L(s_v)L(t_v)\}^{2+\epsilon_v}}.
 \tag{15}
\]
The [exact contracted symbol](research_mixed_contracted_phase.md#2-exact-interpolation-and-its-full-symbol)
is \(N^{-m}a_0e^{NH}(1+O(N^{-1}))\) after taking the absolute
value on the real compact central box. All its factors are positive
and smooth there. Ordinary lattice Laplace asymptotics, (10), and
(11) therefore give
\[
 \mathcal A_N=
 \frac{(2\pi)^m a_0(z_*)}{\sqrt{\det[-H''(z_*)]}}
             e^{NH_*}\{1+O(N^{-1})\}.
 \tag{16}
\]
The power is zero: \(N^{-m}\) from the exact summand, \(N^{2m}\)
from the index lattice, and \(N^{-m}\) from its \(2m\)-dimensional
Gaussian cancel. The positive coefficient in (16) belongs to the
absolute majorant, not to the original oscillatory trace (13).
The offset of the critical point from the lattice causes only the
Gaussian Poisson-summation error; the first cubic correction is odd,
so the full-level relative remainder is \(O(N^{-1})\). Both level parities
and all original finite factorial endpoints have been retained.

## 5. The comparison that this theorem does not supply

The gap in (14) is relative to \(H_*\). To use it as a remainder
bound for a complex critical action \(\mathcal S\), one would
still need \(H_*-1/10000<\Re\mathcal S\), or a stronger coherent
estimate that preserves cancellation among the other indices.
Real concavity proves neither condition. In particular the positive
coefficient of (16) is not a lower bound for the specified original
trace, and the real maximum need not be its complex stationary point.

Run `python3 experiments/check_mixed_real_index_entropy.py`.
The checker verifies the exact tetrahedral/reflection identities,
all endpoint inequalities, incidence and normalization identities,
and source provenance. The full-word and all-level conclusions follow
from the analytic reductions above, not from enumerating finite words.
