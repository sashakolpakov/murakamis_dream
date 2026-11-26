# Fourier cancellation and a strict upper bound for the complete source

Private written proof, 23 November 2026.

The full vertex closing, including its first spectral normals, is a
sampled total derivative. In its Gaussian Fourier representation the
zero alias therefore cancels exactly. Away from explicitly retained
angular cuts and coefficient-band boundaries, its positive Fourier
energy is exponentially concentrated near nonzero integer aliases.

Combining this dual estimate with the exact edge-source estimate gives
a joint real localization of the original marked contraction. This is
an upper bound for its complementary contribution, relative to the
original incidence norm. No geometric lower bound or complex
hyperbolic-cycle coefficient is inferred.

## 1. The original root functional and its canonical Riesz row

Fix the quantum root throughout:
\[
 N\ge2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,\quad
 \eta=(-1)^d,\quad \kappa=q^{d^2/2},\quad
 C_{N,n}=q^{nd^2/4}.
 \tag{1}
\]
Every fractional power means the displayed exponential. The signed
integer \(n\) is fixed before the limit. Let \(\phi_N\) be the
original full Frobenius functional on
\(\mathbb C[X]/(2T_N(X/2)+2)\), and let \(R^n\) be the original
crossing power with its scalar \(\kappa^n\) retained.

Put
\[
 \psi_j=-\pi+(2j+1)\pi/N,\qquad
 G_{N,n}(\psi)=\exp(inN\psi^2/(4\pi)),\qquad 0\le j<N .
 \tag{2}
\]
The actual full-Hermite data of \(R^n\) are those of
\(C_{N,n}G_{N,n}(\psi)\) at \(X=-2\cos\psi_j\).
The double nodes retain their first derivatives. At odd levels the
simple node \(X=-2\), corresponding to \(\psi=0\), retains its value.
These are the fixed-branch data in [S](7)--(8).

For every ordinary polynomial \(A\), the exact derivative sampling is
\[
 \phi_N(R^nA)=
 \eta C_{N,n}\sum_{j=0}^{N-1}
 \left.\partial_\psi
       \{\sin\psi\,G_{N,n}(\psi)A(-2\cos\psi)\}
                                      \right|_{\psi=\psi_j}.
 \tag{3}
\]
For clarity, this also follows directly from [J](12). Write
\(w=-e^{i\psi}\), so \(w-w^{-1}=-2i\sin\psi\) and
\(w\partial_w=-i\partial_\psi\). The fixed original Gaussian in
[S] is
\[
 q^{-nd^2/4}
 \exp\{n(x-\pi i)^2/(2\hbar)\},\qquad
 x=i(\psi+\pi),\quad \hbar=2\pi i/N .
\]
Multiplication by \(\kappa^n\), followed by this substitution in
[J](12), gives (3). At an inversion pair (3) gives the original
value-plus-normal residue. At the odd simple node its summand is
exactly \(R^n(-2)A(-2)\). Thus no auxiliary normal has been added.

Consider a vertex of valence \(h\ge1\). Before identifying its
incidences, use Laurent variables \(z_i=e^{i\theta_i}\) and the
canonical space
\[
 \mathcal V_{N,h}=
 \{f:\text{separately even Laurent polynomials of band }[-d,d]\}.
 \tag{4}
\]
The original vertex functional identifies all
\(X_i=-z_i-z_i^{-1}\), multiplies by \(R^n\), and applies \(\phi_N\).
It uses the whole product before reduction in the physical relation.

Here is a convenient extension to individual Laurent monomials.
For \(m=(m_1,\ldots,m_h)\), put \(s=\sum_i m_i\) and define
\[
 \lambda_{N,n,h}(m)=
 \eta C_{N,n}\sum_{j=0}^{N-1}
 \left.\partial_\psi
   \{\sin\psi\,G_{N,n}(\psi)e^{is\psi}\}
                                             \right|_{\psi_j}.
 \tag{5}
\]
For a separately even polynomial this is exactly the prescribed
functional, by (3). Let \(\Pi_{N,h}\) retain the band and average
independently under \(m_i\mapsto-m_i\). Its canonical Hermitian
Riesz row is
\[
 H_{N,n,h}=\Pi_{N,h}\overline{\lambda_{N,n,h}},\qquad
 \Lambda_{N,n,h}(f)=\langle H_{N,n,h},f\rangle .
 \tag{6}
\]
The inner product is conjugate linear in its first argument.
The evenization in (6) is a fixed average over \(2^h\) orientations.
It does not identify a value-only quotient with the original algebra.

On the band, \(|s|\le hd\). Differentiating (5) bounds each summand
by \(C_{n,h}N\), hence
\[
 |\lambda_{N,n,h}(m)|\le C_{n,h}N^2,\qquad
 \|H_{N,n,h}\|_2^2\le C_{n,h}N^{h+4}.
 \tag{7}
\]
This polynomial bound includes the complete original normal.

## 2. The real alias set and the quantitative statement

Use the exact coefficient-space Gaussian frame of [A] and [E].
In \(h\) variables, with fixed width \(\sigma>0\),
\[
 (\mathcal F_N f)(\theta,\xi)=
 c_N^h\sum_{m\in\mathbb Z^h}
 f_m e^{-|m-N\xi|^2/(2\sigma N)}e^{im\cdot\theta},
 \qquad c_N=(N/(\pi\sigma))^{1/4}.
 \tag{8}
\]
Its measure is \(d\nu=d\xi\,d\theta/(2\pi)^h\), and it is an exact
isometry. The angles below use the principal interval
\([-\pi,\pi)\); the cut is retained explicitly.

For \(\epsilon\in\{\pm1\}^h\), put
\[
 \begin{split}
 r_{n,h}(\theta,\xi)^2
 =\min_\epsilon\inf_{\vartheta\in[-\pi,\pi]}
 \left\{
 \sum_i|\epsilon_i\theta_i-\vartheta|^2+
 \operatorname{dist}\left(
    \sum_i\epsilon_i\xi_i+\frac{n\vartheta}{2\pi},
                          \mathbb Z\setminus\{0\}\right)^2
 \right\}.
 \end{split}
 \tag{9}
\]
Thus its zero set is the oriented copy relation together with a
nonzero integer alias. Both angle and momentum change sign under
an incidence inversion.

For \(0<\delta\le1/4\), retain the following regions:
\[
 \begin{split}
 \mathcal C_\delta&=\{\min_i(\pi-|\theta_i|)\le\delta\},
       &&\text{angular-cut strips},\\
 \mathcal B_\delta&=\{\min_i\bigl||\xi_i|-1\bigr|\le\delta\},
       &&\text{band-boundary strips},\\
 \mathcal L_{n,h,\delta}
       &=\{r_{n,h}\le\delta\}\cup\mathcal C_\delta
                                      \cup\mathcal B_\delta .
 \end{split}
 \tag{10}
\]
The first set keeps the actual spectral-window endpoints. The
second keeps truncation at the full physical coefficient band.

**Theorem 1.** For every fixed \(n,h,\sigma\), there are \(C,A,c>0\)
such that, at every level and \(0<\delta\le1/4\),
\[
 \boxed{\quad
 \int_{\mathcal L_{n,h,\delta}^{\,c}}
       |\mathcal F_NH_{N,n,h}|^2\,d\nu
             \le CN^A e^{-cN\delta^2}.
 \quad}
 \tag{11}
\]
The constants may depend on \(n,h,\sigma\). Neither primality nor
level parity is restricted. The cut strips in (10) are part of
the assertion, rather than errors set equal to zero.

## 3. Known Gaussian sums and the exact zero-alias cancellation

It suffices first to analyze the unaveraged row in (5).
The elementary Gaussian Poisson formula is
\[
 \sum_{m\in\mathbb Z}e^{-(m-N\xi)^2/(2\sigma N)}e^{imu}
 =\sqrt{2\pi\sigma N}\sum_{l\in\mathbb Z}
 e^{-\sigma N(u-2\pi l)^2/2}
                         e^{iN\xi(u-2\pi l)}.
 \tag{12}
\]
It follows by taking the Fourier coefficients of the periodized
Gaussian. Both sides and their fixed derivatives converge normally
on compact real parameter sets. Only known Gaussian test functions
are being transformed.

Work first on \(|\xi_i|\le2\), outside the strips in (10).
If some \(|\xi_i|\ge1+\delta\), the finite band is a distance at
least \(N\delta\) from that Gaussian center. Cauchy--Schwarz and
(7) give the required polynomial times \(e^{-cN\delta^2}\) bound.
It remains to consider \(|\xi_i|\le1-\delta\) for every \(i\).
Replacing the finite \(m_i\)-sum by the full lattice then has the
same bound: every omitted \(m_i\) satisfies
\(|m_i-N\xi_i|\ge N\delta\).
The derivative in (5) adds only fixed polynomial factors in
\(N,|m|,|j|\). Gaussian tail estimates absorb those factors.

In (12), with \(u=\theta_i-\psi_j\), every \(l\ne0\) is also
exponentially small on the original \(j\)-range when
\(\pi-|\theta_i|\ge\delta\). Indeed
\[
 |\theta_i-\psi_j-2\pi l|\ge\delta
                \quad(l\ne0,\ 0\le j<N).
 \tag{13}
\]
The sum over all these aliases and its derivative have a fixed
polynomial cost. For the remaining \(l=0\) term put
\[
 \begin{split}
 \bar\theta&=h^{-1}\sum_i\theta_i,\qquad
 S_\theta=\sum_i(\theta_i-\bar\theta)^2,\\
 j_0&=N(\bar\theta+\pi)/(2\pi)-1/2,\qquad
 \beta=\sum_i\xi_i+n\bar\theta/(2\pi),\\
 a&=2\pi^2\sigma h+i\pi n,\qquad \Re a>0 .
 \end{split}
 \tag{14}
\]
After the explicit constant of unit modulus
\(\Gamma=\exp\{iN\sum_i\xi_i(\theta_i-\bar\theta)
                         -inN\bar\theta^2/(4\pi)\}\) is removed,
the function being differentiated is
\[
 \mathcal H(j)=
 e^{-\sigma NS_\theta/2}
 \sin\psi_j\,
 \exp\{-a(j-j_0)^2/N-2\pi i\beta(j-j_0)\}.
 \tag{15}
\]
Since every \(\theta_i\) is away from the cut, so is
\(\bar\theta\). Extending the \(j\)-sum from \(0,\ldots,N-1\) to
the whole lattice changes the answer by at most
\(CN^A e^{-cN\delta^2}\). This follows directly from its real
Gaussian factor; its derivative has the same tail estimate.

Crucially, the row is the derivative of the entire expression.
After the estimated band, nonprincipal-lift and finite-window
errors are removed, its remaining whole-lattice contribution is
exactly, with the factors from (8) and (12),
\[
 \eta\overline{C_{N,n}}\Gamma\frac{N}{2\pi}
 c_N^h(2\pi\sigma N)^{h/2}
                     \sum_{j\in\mathbb Z}\mathcal H'(j).
 \tag{16}
\]
The function \(\mathcal H\) is Schwartz on the real line. Poisson
summation and integration by parts therefore give
\[
 \sum_{j\in\mathbb Z}\mathcal H'(j)
       =\sum_{k\in\mathbb Z}2\pi i k\,\widehat{\mathcal H}(k)
       =\sum_{k\ne0}2\pi i k\,\widehat{\mathcal H}(k).
 \tag{17}
\]
The zero alias vanishes exactly. This uses the value term, the
first normal and the derivative of the sine together.

To bound the remaining terms, expand
\(\sin\psi_j\) into its two exponentials. Their shifts of
\(\beta\) are exactly \(+1/N\) and \(-1/N\).
The Gaussian Fourier integral, with the square root chosen
continuously from positive real \(a\), is
\[
 \int_{\mathbb R}e^{-ax^2/N}e^{-2\pi i b x}\,dx
       =\sqrt{\pi N/a}\,e^{-\pi^2Nb^2/a}.
 \tag{18}
\]
Here \(\Re(1/a)>0\). Since \(\beta\) stays in a fixed bounded
interval on the present \(\xi\)-box, (17)--(18) imply
\[
 \left|\sum_j\mathcal H'(j)\right|
 \le C N^{1/2}e^{-cNS_\theta}
       \exp\{-cN\operatorname{dist}
                         (\beta,\mathbb Z\setminus\{0\})^2\}.
 \tag{19}
\]
For example, use
\((u\pm1/N)^2\ge u^2/2-N^{-2}\), and sum the remaining Gaussian
tails with their factor \(|k|\). All constants are uniform in
the real centers under consideration.

The Gaussian in [S] must keep its actual logarithmic lift.
At the sampled integers its phase can also be written with
\(j(j+N+1)\), but this changes the interpolating function by
\(e^{2\pi i n j}\). Its derivative then labels the zero alias
incorrectly. The phase used in (15) comes from
\(j(j+1)-Nj\), exactly as fixed in (2)--(3).

## 4. Completion of the dual estimate and a central gap

For the chosen orientation, evaluating the infimum in (9) at
\(\vartheta=\bar\theta\) gives
\[
 r_{n,h}^2\le
 S_\theta+
       \operatorname{dist}(\beta,\mathbb Z\setminus\{0\})^2.
 \tag{20}
\]
Thus (19) is exponentially small off \(\{r_{n,h}\le\delta\}\).
The band and cut errors above have the same estimate.
Evenization replaces \((\theta_i,\xi_i)\) by
\((\epsilon_i\theta_i,\epsilon_i\xi_i)\) and averages finitely
many terms. The definition (9) keeps all of them.

Integration on \(|\xi_i|\le2\) costs only its fixed finite volume.
Outside that box, angular Parseval and the original coefficient
band give
\[
 \int_{\max_i|\xi_i|>2}|\mathcal F_NH_{N,n,h}|^2\,d\nu
                 \le Ce^{-cN}\|H_{N,n,h}\|_2^2 .
 \tag{21}
\]
This is the same elementary Gaussian tail estimate as [E](20).
Equations (7) and (13)--(21) prove Theorem 1, including the
regime where \(N\delta^2\) is bounded.

There is a useful actual cancellation consequence. Choose
\[
 0<r\le
 \min\{\pi/4,\,[4(h+|n|+1)]^{-1}\}.
 \tag{22}
\]
On the central box \(|\theta_i|,|\xi_i|\le r\), every orientation
has its mean angle in this interval and
\(|\beta|\le hr+|n|r/(2\pi)<1/2\).
The proof above, with its cuts and band boundaries separated by
fixed distances, gives
\[
 \int_{\substack{|\theta_i|\le r\\|\xi_i|\le r}}
            |\mathcal F_NH_{N,n,h}|^2\,d\nu
                         \le CN^A e^{-cN}.
 \tag{23}
\]
This is the closing's cancellation of the central zero-alias
packet. It is not obtained by bounding its separate normal
channels in absolute value.

## 5. Joint localization with the original edge source

Use the root specialization of the original compiler [F] on a fixed
finite graph. At vertex \(v\), keep its prescribed signed power
\(R^{n_v}\) and all \(h_v\) incidence variables until the original
identification and trace. Any isolated vertex contributes its
unchanged scalar trace, of polynomial size; it may be factored
out. Let \(\Lambda_N\) be the resulting original marked functional.
The complete row on the remaining incidence space is the tensor
product of (6), with its prescribed outside root scalars retained.

Let \(F_N\) be the actual same-index source [E](2), allowing arbitrary
activity-independent coupled coefficients. Write \(p_{e,0}\) for the
full real edge symbol [E](4), including its prefactor. Set
\[
 \Omega_\delta=
 \{\max_e|p_{e,0}|<\delta\}
       \cap\bigcap_v\mathcal L_{n_v,h_v,\delta}.
 \tag{24}
\]
The incidence Gaussian frame tensorizes. Theorem 1 and the polynomial
row bounds therefore control its dual mass off any vertex region.
The edge theorem [E](5) controls the primal mass off the edge region.
Applying Cauchy--Schwarz in the exact frame pairing proves
\[
 \boxed{\quad
 |\Lambda_N(F_N)-\Lambda_N(Q_{\Omega_\delta}F_N)|
       \le C N^A e^{-cN\delta^2}\|F_N\|_2,\qquad
 Q_\Omega=\Pi_N\mathcal F_N^\dagger
                         \mathbf1_\Omega\mathcal F_N\Pi_N .
 \quad}
 \tag{25}
\]
Here \(\Pi_N\) is the full incidence band-and-even projection.
Its row and input are both canonical, so
\(\Lambda_N(Q_\Omega F_N)\) is exactly the restricted frame pairing.
One uses the primal off-edge estimate on that part of the complement,
and the dual off-vertex estimate on the rest. No cutoff is commuted
through a vertex tensor or through the closing.

The constants depend on the fixed graph, powers and Gaussian width,
not on the coupled coefficient array. The original complete main-color
root scalar has its compiler framing and reduced-cut factors unchanged.
The assertion is at the fixed root; it does not infer a moving-meridian
identity from activity-independent normal insertion weights.

## 6. A strict upper gap below the unfilled circle-graph rate

There is a source-specific consequence beyond complementary-region
localization. Use precisely the original root circle compiler [F],
with at least one edge, all its vertex traces closed, and any fixed
signed integer powers. There is no largeness or hyperbolicity
assumption on those powers. Write
\[
 \begin{gathered}
 I=[1/5,3/10],\qquad
 g(x)=2\int_0^x\log(\cot\pi t)\,dt,\quad 0\le x\le1/2,\\
 G_0=\max_{0\le x\le1/2}g(x)=g(1/4)
                  =\frac{2G_{\mathrm{Cat}}}{\pi},\qquad
 F_0=2|E|G_0=\frac{4|E|G_{\mathrm{Cat}}}{\pi}.
 \end{gathered}
 \tag{26}
\]
The endpoint integrals defining \(g\) are improper integrals.
Here \(G_{\mathrm{Cat}}=\int_0^{\pi/4}\log(\cot u)\,du\) is
Catalan's constant. The substitution \(u=\pi t\) gives the displayed
value of \(G_0\); \(g'(x)=2\log(\cot\pi x)\) fixes its unique maximum.
This is the original Newton entropy in [F]. Then there are
\(C,A,\eta_*>0\), depending on the fixed compiler and powers, such that
\[
 \boxed{\qquad |K_N|\le CN^A e^{N(F_0-\eta_*)}.\qquad}
 \tag{27}
\]
The same estimate holds for the compiler scalar before its prescribed
root framing phase. This is a strict gap from the unfilled circle
envelope \(F_0\); it is not a comparison with the filled volume.

Here is the full retained-source proof. In separate incidence
variables let
\[
 f_N=\prod_{e}\sum_{k/N\in I}B_k(z_e)B_k(y_e),\qquad
                     b_N=f_N(\mathbf1)>0 .
 \tag{28}
\]
At the root the actual edge weights \(H_N/W_k\) and their scalar
turn factors are one. The original powers remain in \(\Lambda_N\).
The root specialization of [F] bounds the complete sum of all
discarded index assignments by
\(CN^A e^{N(F_0-\eta_0)}\), with its fixed \(\eta_0>0\).
It is thus enough to prove (27) for \(\Lambda_N(f_N)\).

The factor-pairing proof in [P] gives nonnegative Laurent
coefficients for each \(B_k\), \(k/N\in I\), once \(N\) is
sufficiently large. A negative cosine parameter is paired with a
positive one before expanding; the paired quadratic Laurent product
has positive coefficients. All remaining single parameters are
nonnegative. In particular \(B_k/B_k(1)\) is the generating function
of a symmetric probability measure. Its same proof gives
\[
 \frac{B_k(e^t)}{B_k(1)}\le e^{4Nt^2},\quad |t|\le1/4,
 \qquad
 |B_k(e^{i\theta})|
       \le B_k(1)e^{-aN d_{\mathbb T}(\theta,0)^2}
 \tag{29}
\]
with an absolute \(a>0\). The latter is [P]'s full-period raw
angular bound. Positivity preserves both estimates under the retained
edge sum and products. Consequently the coefficients \(f_{N,m}\)
are nonnegative, \(\sum_m f_{N,m}=b_N\), and
\[
 |f_N(e^{i\theta})|\le b_N e^{-aN\sum_i\theta_i^2},\qquad
 \|f_N\|_2\le b_N,\qquad
 \frac{f_N(1,\ldots,e^t,\ldots,1)}{b_N}\le e^{4Nt^2}.
 \tag{30}
\]
Every incidence belongs to exactly one edge factor; the last bound
therefore holds separately in each coordinate, despite the shared
index within an edge.

We record both Fourier-energy marginals rather than infer them
from a pointwise transform. If \(J=2|E|\) is the number of incidences,
direct Gaussian integration in (8) gives exactly
\[
 \int_{\mathbb R^J}|\mathcal F_N f(\theta,\xi)|^2d\xi
                 =e^{\Delta_\theta/(4\sigma N)}
                                      |f(e^{i\theta})|^2 .
 \tag{31}
\]
Indeed the \(m,m'\) entry is multiplied by
\(\exp(-|m-m'|^2/(4\sigma N))\). This is the positive periodic
heat kernel. Convolving its Gaussian bound with (30) proves that,
for every fixed \(r>0\), the Fourier energy where some
\(|\theta_i|\ge r\) is at most \(CN^A e^{-cNr^2}b_N^2\).
One may check the convolution by completing the square in each
periodic Gaussian lift; all other lifts have the same tail bound.

For the other marginal, positivity and the last bound of (30),
with \(t=r/16\), give
\[
 \sum_{|m_i|\ge rN/2}f_{N,m}
                      \le2e^{-Nr^2/64}b_N,\qquad 0<r\le1 .
 \tag{32}
\]
The estimate is just
\(\exp(-trN/2+4Nt^2)\) for each of the two tails.
Split \(f_N\) into these high coefficients and their complement.
The high part has coefficient norm at most the left side of (32).
For the low part, angular Parseval in (8) leaves Gaussian centers
\(|m_i|\le rN/2\); integration over \(|\xi_i|\ge r\) is
exponentially small. The frame isometry bounds the high part
without any change of metric. Union over the fixed incidences,
and (31), therefore show
\[
 \int_{\{\max_i(|\theta_i|,|\xi_i|)>r\}}
           |\mathcal F_Nf_N|^2d\nu
                      \le CN^A e^{-cNr^2}b_N^2 .
 \tag{33}
\]

Choose one positive-valence vertex and fix \(r\) as in (22) for
its actual power. Such a vertex exists because \(E\ne\varnothing\).
The row on the whole graph is a tensor product. Its full norm is
polynomial by (7), while its mass in the central box of all
incidences is exponentially small by (23) at this one vertex.
Use exact frame pairing and Cauchy--Schwarz on that box and its
complement. Equation (30) controls the primal full norm; (33)
controls its complementary norm. We obtain
\[
                  |\Lambda_N(f_N)|\le CN^A e^{-c_*N}b_N
                         \qquad(c_*>0).
 \tag{34}
\]
No separate first-normal term was dropped: the dual estimate on
the central box used their exact total derivative.

Finally [F]'s uniform entropy comparison gives
\(B_k(1)=\exp\{Ng(k/N)+O(\log N)\}\) on \(I\).
The positive sum in (28) has an index within \(O(N^{-1})\) of
the unique maximum \(1/4\). Thus
\[
                       b_N=e^{NF_0+O(\log N)} .
 \tag{35}
\]
Combine (34)--(35) with the original discarded-assignment bound,
and take \(\eta_*=\min(c_*,\eta_0)>0\), decreasing it if needed
to absorb fixed polynomial prefactors. The original external root
framing has modulus one and is retained. This proves (27).
Increasing \(C\) covers the finitely many small levels.

The gap is not asserted uniform in unbounded powers or changing
graphs. It proves neither nonvanishing of \(K_N\) nor the required
filled-volume rate. It differs from the existing charge-increment
norm, which has the unfilled rate, and from the prior braid
crossing-count bound: the envelope here counts this compiler's
circle edges.

There is a useful uniform-rate consequence after fixing a short
coordinate. Write \(V\) for the vertex set of this fixed compiler
graph, choose a positive-valence vertex \(v_0\), and fix its signed
integer power \(n_0\). Then there is \(\eta_{v_0,n_0}>0\), independent
of every other fixed signed power, such that
\[
 \boxed{\quad
 \sup_{\mathbf m\in\mathbb Z^{\,V\setminus\{v_0\}}}
 \limsup_{N\to\infty}\frac1N
           \log|K_N(n_0,\mathbf m)|
                  \le F_0-\eta_{v_0,n_0}.
 \quad}
 \tag{36}
\]
Here \(\log0=-\infty\), and each completion \(\mathbf m\) is held
fixed before \(N\) tends to infinity.

Indeed choose \(r\) in (22) using only \(v_0,n_0\). The central
dual exponent (23) then uses only that vertex. All other rows enter
through (7), where their powers affect polynomial prefactors rather
than exponential rates. The source concentration (29)--(33) contains
no crossing power. The discarded-index loss \(\eta_0\) in [F] is
also independent of the fixed powers. Thus the same positive loss
can be used in (34) and (27) for every fixed completion. The
prefactors and starting level may depend on that completion.
Restricting the supremum to any additional fixed partial assignment
preserves (36).

The order of quantifiers is essential. Equation (36) does not
interchange the supremum with the \(N\)-limit, permit powers that
vary with \(N\), or give a uniform finite-level prefactor. Its
reference rate is still the unfilled envelope \(F_0\), rather than
the volume of a partially or completely filled hyperbolic manifold.

## 7. Scope and complete sources

The nonzero alias is defined on the retained angular lift. It cannot
be relabeled cyclically while discarding the cut currents. Equation
(25) retains those strips, every physical coefficient and every first
spectral normal. The permitted vertex regions depend on the actual
signed powers; their zero alias is absent for every such power.

This supplies a real joint complementary-region estimate for the
original source. It does not identify its incidence energy with an
ordinary-color Plancherel energy, compare the retained region with a
complex Casson--Rivin chart, or prove a nonzero geometric contribution.
The band and angular-cut regions in (10) require their own estimates
if they are to be removed. No arbitrary short-component volume theorem
or finite-exception theorem follows from (25).

The following complete proof texts were read at matching pins:

* [S], [Signed original Gaussian and its full Ward data](research_signed_gaussian_ward_endpoint_packet.md),
  503 lines, SHA256
  6bdced1b01917e41631386a24b337b60dfe5b04d35d70007cb56badc511a0191.
* [J], [Original first-order jets and full closing](research_first_order_gaussian_jet_transport.md),
  365 lines, SHA256
  baf7987b6550df2ee7a11f5433b27b04938d1ca54697b129c42a955bd5ad3d10.
* [F], papers/circle-tree-asymptotics/finite-bounds.tex,
  227 lines, SHA256
  e4cf66544703af6d9a78208deae971c4d9f4367ba4b2ad660694ee489ef67ea1.
* [E], [Exponential actual edge-source bound](research_same_index_edge_exponential_characteristic_bound.md),
  474 lines, SHA256
  f349e8fa328b0acd4f3d4519eb2c074504e56d44d5f4d2ae643e4e9d87516d2e.
* [A], [Exact incidence Gaussian frame and edge equation](research_same_index_edge_fourier_characteristic_bound.md),
  302 lines, SHA256
  2e5788e51a5586966b53f0eb5a864b83415c134a083de939fca141cc7ae434ee.
* [P], papers/circle-tree-asymptotics/edge-packet.tex,
  268 lines, SHA256
  53eb6dbfbda3ca639db35911ed50947c29655840337f9d1f1ce909d435013dbb.

Whole comparison texts were also retained at matching pins:
[Full-period currents and charge convolution](research_full_period_current_charge_convolution.md),
596 lines, 3f74b9824ecbf0b71a79b17959c7208f650103f95932192cfba87c7a7aa05595;
[Gaussian Newton frame and original operators](research_gaussian_frame_newton_transport.md),
335 lines, b6ed7fa19097323f76b0b22fb4fc7361b9d4e52c3f19d17c12d94c6fff623af9;
[Gabor source sewing](research_finite_gabor_pointed_source_sewing.md),
455 lines, 8a954f9f2bec9e0fc8971b08ea0ca493f712d4e2ace6bb9fc2c1fcf705699c37;
the [Charge-increment graph norm](research_charge_increment_graph_norm.md),
355 lines, 8636d7606113873e8fa3ed3512dcf22b3eb359efac6d1dce4499fc321f00100c;
and [Complete-source real saddle exclusion](research_complete_source_real_saddle_exclusion.md),
528 lines, 9e15defd27cabf3425f11be830fc8d385948023c791fb3fb4e8d696ea2b13572.
These already supply exact derivative sampling, current bookkeeping,
positive frames and comparisons with other source envelopes.
The added estimates are the exponentially localized dual row with its
zero alias canceled before absolute values, the joint source bound
(25), and the whole-scalar strict circle-envelope gap (27), including
its anchored rate consequence (36).

Only written mathematics and source-text/hash operations were used.
No mathematical program, numerical experiment, test, build, git
operation, or edit of an adopted source was performed.
