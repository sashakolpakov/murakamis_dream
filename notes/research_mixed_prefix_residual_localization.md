# Residual localization of an original canonical prefix

Research lemma, 6 November 2026. The original uniform Hessian bound
turns a small original-gradient residual into a certified distance to
the already existing canonical prefix. No additional local existence
test, polynomial-root selection, or inverse-matrix computation is
needed. This note specifies a bounded diagnostic, not its outcome.

## 1. The seven original gradient coordinates

Let the first three vertex flags be \((\alpha,1,\beta)\), with
\(\alpha,\beta\in\{0,1\}\), and fix the next external leg \(c\).
Order the seven unknowns as
\[
 q=(e,\xi,a,u,z,v,b),\qquad
 (a,u,z,v,b)=(r_1,s_2,r_2,s_3,r_3).
 \tag{1}
\]
Write \(j(w)=J'(w)=\Log(2\sin\pi w)\) on the original regular
strip. Put
\[
\begin{split}
 B(e,\xi)&=-2J(1/2-\xi)-3J(\xi)-J(e-\xi),\\
 F(q;c)&=B(e,\xi)+J(e+a)-\alpha[J(e)+J(a)]\\
 &\quad+J(u+z)-J(u)-J(z)+J(v+b)-\beta[J(v)+J(b)]\\
 &\quad+J(a+u)-2J(a)-2J(u)
       +J(z+v)-2J(z)-2J(v)\\
 &\quad+J(b+c)-2J(b)+i\pi Q(q;c),\\
 Q(q;c)&=e\xi-ea+au-uz+zv-vb+bc\\
 &\quad+\frac\alpha2(e^2+a^2-e-a)
       +\frac12(u^2+z^2-u-z)
       +\frac\beta2(v^2+b^2-v-b).
\end{split}
 \tag{2}
\]
This is the restriction of the original length-four action in the
[common-domain Hessian theorem](research_mixed_open_word_hessian.md),
equation (1), up to terms depending only on the fixed coordinates.
In particular the omitted \(-2J(c)\) has no effect on its seven
gradient components. Direct differentiation gives, in the order (1),
\[
\begin{split}
 f_e={}&-j(e-\xi)+j(e+a)-\alpha j(e)
        +i\pi[\xi-a+\alpha(e-1/2)],\\
 f_\xi={}&2\Log\cos\pi\xi+\Log\sin\pi(e-\xi)
             -3\Log\sin\pi\xi+i\pi e,\\
 f_a={}&j(e+a)+j(a+u)-(2+\alpha)j(a)
        +i\pi[u-e+\alpha(a-1/2)],\\
 f_u={}&j(u+z)+j(a+u)-3j(u)+i\pi[a-z+u-1/2],\\
 f_z={}&j(u+z)+j(z+v)-3j(z)+i\pi[v-u+z-1/2],\\
 f_v={}&j(v+b)+j(z+v)-(2+\beta)j(v)
        +i\pi[z-b+\beta(v-1/2)],\\
 f_b={}&j(v+b)+j(b+c)-(2+\beta)j(b)
        +i\pi[c-v+\beta(b-1/2)].
\end{split}
 \tag{3}
\]
Thus \(f=\nabla_qF\) exactly, with no diagonal rescaling. For the
auxiliary component, differentiation first gives
\(2j(1/2-\xi)-3j(\xi)+j(e-\xi)+i\pi e\); the three
\(\log2\) constants cancel. This recovers the original endpoint
equation (6) of
[open-word critical localization](research_mixed_open_word_critical_localization.md).
Its interior equations (3) supply the other four ordinary components.

Use the same closed convex product
\[
 \mathcal D=E\times U\times Q^5,\qquad
 E=[.33,.47]+i[-.09,.08],\quad
 U=[.21,.25]+i[.01,.10],\quad
 Q=[.23,.45]+i[-.12,.12].
 \tag{4}
\]
For \(q\in\mathcal D\) and \(c\in Q\), all arguments of
\(j\) in (3) have real part strictly between zero and one.
The corresponding sine has positive real part. The sine and cosine
arguments in \(f_\xi\) likewise have positive real part; in
particular \(\Re(e-\xi)\in[.08,.26]\). Principal logarithms
therefore give the original holomorphic branches throughout a
neighborhood of the product. No exponential equation is substituted
for (3).

## 2. Existing existence and a quantitative residual theorem

Put \(\mu=6\pi/49\). For fixed \(c\in D_3\cup D_4\),
the [reference-curve theorem](research_mixed_second_selected_reference_curve.md),
Section 4, supplies a unique zero \(q_*(c)\in\mathcal D\) of
(3). Its existence uses the simultaneous update of the three
disjoint groups
\[
 (e,a,\xi)=\operatorname{endpoint}_\alpha(u),\qquad
 (u,z)=\operatorname{ordinary}_1(a,v),\qquad
 (v,b)=\operatorname{ordinary}_\beta(z,c).
 \tag{5}
\]
The original endpoint maps and the full-disk-product ordinary maps
of [cyclic critical localization](research_mixed_cyclic_critical_localization.md),
Lemma 2, make this a continuous self-map of
\(E\times U\times D_{3+\alpha}\times D_4^2
\times D_{3+\beta}^2\), in the order (1).
Brouwer gives a zero; the uniform original Hessian gives uniqueness.
No contraction of the combined iteration (5) is asserted.

**Theorem 1.** For either flag pair, every \(c\in D_3\cup D_4\)
and every \(q_0\in\mathcal D\),
\[
       \|q_0-q_*(c)\|_2\le\frac{\|f(q_0;c)\|_2}{\mu}.
 \tag{6}
\]
If \(q_0\ne q_*(c)\), the inequality is strict.

Indeed the \(q\)-Hessian of (2) is a principal block of the original
length-four Hessian with \(s_4=c\) and the remaining right-end
coordinates fixed in their common rectangles. Hence, on the whole
convex product, \(-\Re F_{qq}''\succ\mu I_7\). For a complex
symmetric matrix its Hermitian part equals its entrywise real part.
With \(d=q_0-q_*\), integration along the complex segment therefore
gives
\[
 \mu\|d\|_2^2
 <\Re\{d^*[-f(q_0;c)+f(q_*;c)]\}
 \le\|d\|_2\,\|f(q_0;c)\|_2
 \quad(d\ne0).
 \tag{7}
\]
This proves (6). The estimate uses the original full gradient and its
original existence theorem. A small residual without that existence
input would not establish a zero. The proof is unchanged if \(q_0\)
lies on the boundary of \(\mathcal D\).

**Uniform parameter consequence.** Let \(K\subset D_3\cup D_4\)
and let a prescribed approximation \(q_0(c)\) stay in \(\mathcal D\).
If an outward bound proves
\[
       \sup_{c\in K}\|f(q_0(c);c)\|_2<\mu r,
 \tag{8}
\]
then every canonical prefix is within Euclidean distance \(r\) of
its corresponding approximation. In particular a fixed rational
center and a whole external-coordinate box give a simultaneous
enclosure whenever that box is contained in the original input domain.
This does not require a new parameter-cover or root-existence argument;
the required residual bound itself is still an additional calculation.

## 3. A bounded fixed-point diagnostic specification

For the [prescribed canonical reference](research_mixed_second_selected_canonical_reference_fallback.md),
take \(\alpha=1\), \(c=1/3\), and exactly the two cases
\(\beta=0,1\). The fixed input lies in \(D_3\); the canonical
solutions exist before any numerical proposal. Initialize (1) at
\[
 (.35-.035i,\ .225+.036i,\ .30-.052i,\ .30-.052i,
       \ .30-.052i,\ t_\beta,\ t_\beta),
 \quad
 t_0=.35-.01i,\quad t_1=.30-.052i.
 \tag{9}
\]
The separate [diagnostic driver](../experiments/certify_mixed_second_selected_canonical_reference.py)
specifies at most 30 proposal steps at 80 decimal digits, requested
residual tolerance \(10^{-65}\), and 60-digit decimal rational
centers. Those proposals have no proof role. There is no alternate
external input, initialization search, subdivision or precision retry.

Set \(r=10^{-40}\). For each saved exact center, check that its
coordinate radius-\(r\) squares lie strictly in (4), and evaluate
only the original residual (3), outward at 256 bits. If
\([l_j,u_j]\) encloses each of the fourteen real and imaginary
components, form the exact rational bound
\[
 R^2=\sum_{j=1}^{14}\max(|l_j|,|u_j|)^2.
 \quad\text{Accept only if}\quad
 R^2<\mu_-^2r^2,
 \tag{10}
\]
where \(0<\mu_-\le6\pi/49\) is an outward rational lower bound.
Theorem 1 then puts the canonical zero in the Euclidean radius-\(r\)
ball and therefore in every reported coordinate square. Failure of
the proposal, domain check or strict residual test gives no certificate.

The driver binds the completed original geometric author and replay,
their proof/script/dependency hashes, this lemma and the reference
theorem. It does not rerun those certificates. A later saved-center
check would use the same criterion without new floating proposals;
no such additional execution is implied here.

Successful localization identifies a genuine canonical prefix with
the original logarithmic lift. It does not prove that \(c=1/3\)
is realized by a particular finite suffix, a scalar central gap,
or a full-domain or finite-source estimate.
