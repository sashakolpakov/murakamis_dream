# Coherent endpoint inputs have a controlled bulk crossing norm

Written proof, 24 November 2026.

A small endpoint input need not stay near the endpoints after an
original crossing. Here the entire outgoing packet has an explicit
positive exponential norm rate, uniformly for every coherent input
in a sublinear endpoint band. This includes coefficients and phases
chosen separately at each level. A bounded checked Hurwitz observable
controls cancellation between the actual crossing columns.

The original binomial cut also has an exact weighted-cup realization.
Its censored finite endpoint approximation gives the same outgoing
norm rate for the full purified cut, with an arbitrarily small
absolute error after crossing. The ordinary cap, pivot and all
crossing phases remain explicit. No lower bound for a returned cap
or an original closed knot scalar is inferred.

## 1. Actual physical matrices and the statement

Fix \(N\ge3\), \(d=N-1\), and
\[
 q=e^{\pi i/N},\quad Q=q^2,\quad x=-q^{-1},\quad
 \kappa=q^{d^2/2},\quad
 F_j=(Q;Q)_j,\quad S_j=|F_j|,\quad S_0=1 .
 \tag{1}
\]
The original balanced head basis is orthonormal. Pair vectors have
the product Hilbert norm, denoted \(\|\cdot\|\). This is not the
Newton coefficient norm or the Hilbert--Schmidt norm of one box.
The latter will only supply an upper bound for an operator norm.

Let \(R=R_N^+\) be the original checked positive crossing, including
its common Cartan line. On each head retain
\[
 E|a\rangle=(Q^{-a}-1)|a-1\rangle,\quad
 F|a\rangle=(1-Q^{a+1})|a+1\rangle,\quad
 K|a\rangle=xQ^{-a}|a\rangle ,
 \tag{2}
\]
with missing extreme arrows zero. Operator subscripts below label
the physical heads. Write \(\mathsf P\) for the
physical head flip. The exact negative crossing is
\[
                     R_N^-=\mathsf P\,\overline R\,\mathsf P .
 \tag{3}
\]
Conjugation here is entrywise in this physical basis, not adjoint.
These source identities are those of [G,P].

Define the two sign-adapted input bands by
\[
 H_m^+=\operatorname{span}\{|d-a,a\rangle:0\le a<m\},\qquad
 H_m^-=\mathsf P H_m^+,\qquad 1\le m\le N/2 .
 \tag{4}
\]
All these vectors have total physical degree \(d\). Put
\[
 h(t)=\int_0^t\log(2\sin\pi y)\,dy,\qquad
 h_*=h(5/6)=-h(1/6)>0,\qquad
 \Lambda_{N,m}=m\log(eN/m)+\log N .
 \tag{5}
\]

**Theorem.** An absolute constant \(C\) exists such that, for all
sufficiently large \(N\), all \(1\le m\le N/2\), and either sign,
\[
 e^{Nh_*-C\Lambda_{N,m}}\|v\|
       \le \|R_N^\pm v\|
       \le e^{Nh_*+C\Lambda_{N,m}}\|v\|,
                 \qquad v\in H_m^\pm .
 \tag{6}
\]
In particular, for every \(m_N=o(N)\), uniformly over all nonzero
vectors in the corresponding bands,
\[
 \frac1N\log\frac{\|R_N^\pm v_N\|}{\|v_N\|}
                          \longrightarrow h_* .
 \tag{7}
\]
This is an estimate for the full outgoing vector. It does not
compress that vector back to an endpoint band.

## 2. The exact joint high/low kernel

Let \(f_a=R|d-a,a\rangle\), and use \(|i,d-i\rangle\) as output
basis on this degree block. Substitution in the actual entry [G,(2)]
gives, with every phase retained,
\[
 f_a(i)=
 \kappa x^{i-a-d}Q^{a(d-i)}
        \frac{F_iF_{d-a}}{F_{i-a}F_aF_{d-i}}
                 \quad(a\le i\le d),\qquad
 f_a(i)=0\quad(i<a).
 \tag{8}
\]
No factorial at \(N\) occurs. The exact sine reflection
\(S_jS_{d-j}=N\) therefore gives
\[
                  |f_a(i)|=\frac{S_i^2}{S_{i-a}S_a^2}
                             \quad(i\ge a).
 \tag{9}
\]
For example \(f_0\) has output moduli \(S_i\), including its bulk
maximum near \(i=5N/6\). At fixed \(a\) and fixed upper-hole index
\(b=d-i\), (9) is equivalently
\(N S_{a+b}/(S_a^2S_b^2)\). Thus a fixed-endpoint matrix limit
without additional scaling is not the norm statement being proved.

We first control each whole column. Uniformly for \(0\le i<N\),
\[
                    \log S_i=Nh(i/N)+O(\log N).
 \tag{10}
\]
Here is an elementary endpoint-uniform justification. Subtract
\(\log t+\log(1-t)\) from \(\log(2\sin\pi t)\); the remainder
extends smoothly to \([0,1]\). Its Riemann-sum error is bounded.
For each of the two logarithms, integral comparison with
\(\log(j!)\) gives error \(O(\log N)\), uniformly in the stopping
index, including \(i=0,N-1\). Adding these three estimates proves
(10). Also \(h(1)=0\), by the sine double-angle identity and
reflection; hence \(h(1-t)=-h(t)\). Its derivative shows that its
unique global maximum on \([0,1]\) is \(h_*\) at \(5/6\).
The derivative is negative on \((0,1/6)\), proving \(h_*>0\).

For \(1\le a\le N/2\), the sine chord bound gives
\[
 S_a\ge(4/N)^a a!,\qquad
 \frac{S_i}{S_{i-a}}\le2^a,\qquad
 |f_a(i)|\le \max_j S_j\,
              \exp\{2a\log(eN/a)+Ca\}.
 \tag{11}
\]
The last inequality uses \(a!\ge(a/e)^a\). For \(a=0\) its
interpretation is simply \(|f_0(i)|=S_i\).

For the converse choose \(i_*=\lfloor5N/6\rfloor\).
When \(a\le N/2\), every factor of \(S_{i_*}/S_{i_*-a}\)
lies on a fixed compact interval inside \((0,1)\), once \(N\)
is large. Each is bounded below by a fixed positive constant.
Since \(S_a\le2^a\), (9)--(10) imply
\[
 |f_a(i_*)|\ge \exp\{Nh_*-Ca-C\log N\}.
 \tag{12}
\]
Summing at most \(N\) squares in the upper bound and keeping this
one entry for the lower bound now gives, simultaneously for
\(0\le a<m\le N/2\),
\[
 e^{Nh_*-C\Lambda_{N,m}}\le \|f_a\|
                         \le e^{Nh_*+C\Lambda_{N,m}}.
 \tag{13}
\]
Column estimates alone would not justify (6): the columns have
their actual complex phases and can interfere.

## 3. A bounded physical observable separates the columns

There is an exact checked identity on the whole pair:
\[
 A:=R K_1R^{-1}=K_2-qE_2K_1F_1,\qquad
                             \|A\|\le5 .
 \tag{14}
\]
The bound follows from \(\|K\|=1\) and
\(\|E\|,\|F\|\le2\). We verify the ordering and the finite
endpoints directly rather than importing a commuting symbol.

For an input \(|a_0,b_0\rangle\), put \(n=a_0+b_0\). Its
successive positive-transfer outputs are \(|b_0+k,a_0-k\rangle\).
The exact entry ratio from [G,(2)] is
\[
 \frac{r_{k+1}}{r_k}
   =xQ^{-b_0}
       \frac{(1-Q^{b_0+k+1})(1-Q^{a_0-k})}{1-Q^{k+1}} .
 \tag{15}
\]
On \(|i,j\rangle\), the right side of (14) has diagonal
\(xQ^{-j}\) and the additional coefficient
\[
 Q^{-i-1}(1-Q^{i+1})(Q^{-j}-1)
                   \quad\hbox{to }|i+1,j-1\rangle .
 \tag{16}
\]
Using \(x^2Q=1\), (15) says exactly that this output column
is an eigenvector with eigenvalue \(xQ^{-a_0}\). Its first
coefficient has that diagonal eigenvalue already. At the last
allowed transfer the extra coefficient vanishes because \(j=0\)
or \(i=d\). Thus the identity \(AR=RK_1\) holds on every input,
including both endpoints. The original crossing is invertible,
which proves (14).

In degree \(d\), (16) simplifies further:
\[
 A|i,d-i\rangle
   =\zeta_i|i,d-i\rangle+s_{i+1}^2|i+1,d-i-1\rangle,\qquad
 \zeta_i=-qQ^i,\quad s_j=2\sin(\pi j/N).
 \tag{17}
\]
The last term at \(i=d\) is zero. The \(N\) eigenvalues are
distinct, and the actual columns satisfy \(Af_a=\zeta_a f_a\).

Let \(u_a=f_a/\|f_a\|\), and \(V_m c=\sum_{a<m}c_a u_a\).
The internally normalized column Gram has the quantitative bound
\[
                e^{-C\Lambda_{N,m}}I
                    \ \preceq\ V_m^*V_m\ \preceq\ mI .
 \tag{18}
\]
For completeness, use the selected Lagrange polynomials
\[
 L_a(z)=\prod_{\substack{0\le b<m\\b\ne a}}
                   \frac{z-\zeta_b}{\zeta_a-\zeta_b}.
 \tag{19}
\]
They recover the selected column exactly:
\(L_a(A)u_b=\delta_{ab}u_b\), for \(b<m\).
For these consecutive endpoint roots,
\[
 |\zeta_a-\zeta_b|\ge4|a-b|/N,\qquad
 \|A-\zeta_b I\|\le6 .
 \tag{20}
\]
Thus, with the empty product interpreted as one,
\[
 \|L_a(A)\|
 \le\frac{(3N/2)^{m-1}}{a!(m-1-a)!}
 \le\frac{(3N)^{m-1}}{(m-1)!}
 \le \exp\{Cm\log(eN/m)\}.
 \tag{21}
\]
The estimate is a product of operator factors; a scalar supremum
on the spectrum would not suffice for this nonnormal matrix.
Applying (21) to \(V_mc\), then summing
\(|c_a|^2\le\|L_a(A)\|^2\|V_mc\|^2\), gives the lower bound
in (18). The upper bound follows by triangle and Cauchy--Schwarz.
No filter is asserted to annihilate unselected eigenvectors.

For \(v=\sum_{a<m}v_a|d-a,a\rangle\), apply (18) to coefficients
\(c_a=v_a\|f_a\|\), then use (13). Absorbing the polynomial
factors into \(C\Lambda_{N,m}\) proves (6) for the positive sign.
Equation (3) sends \(v\) to \(\mathsf P\bar v\) without changing
norms or support widths, proving the negative case. Since
\(\Lambda_{N,m_N}=o(N)\) when \(m_N=o(N)\), (7) follows.

The filter argument is the same finite-dimensional mechanism used
in [C]. The new estimate concerns actual high/low crossing columns
and their common bulk rate, not a new interpolation method.

## 4. The original cup gives the purified cut exactly

At the complete root retain the literal source tensors [P]:
\[
 p=N\sum_{a=0}^d x^{-a}|d-a,a\rangle,\qquad
 \ell_{ij}=x^i\mathbf1_{i+j=d}/N,\qquad
 g=K^{1-N},\quad g_a=x^{2a-d}.
 \tag{22}
\]
Fix \(L<\infty\), and take real \(0\le\lambda\le L\).
For sufficiently large \(N\), define the original binomial
probabilities and their positive square root by
\[
 \beta_{N,a}=\binom da(\lambda/N)^a(1-\lambda/N)^{d-a},
 \quad H_N=\operatorname{diag}(\sqrt{\beta_{N,a}}),\quad
 P_N=H_N^2 .
 \tag{23}
\]
Then the unit vector
\[
 \Psi_N^+=N^{-1}(I\otimes H_N)p
       =\sum_a x^{-a}\sqrt{\beta_{N,a}}|d-a,a\rangle
 \tag{24}
\]
has the exact physical dual and evaluation
\[
 (\Psi_N^+)^*=N\ell(I\otimes gH_N),\qquad
 (\Psi_N^+)^*(I\otimes C)\Psi_N^+
                               =\operatorname{Tr}(P_NC)
 \tag{25}
\]
for every finite head matrix \(C\). Indeed the coefficient of
the dual on \(|d-a,a\rangle\) is
\(x^{d-a}x^{2a-d}\sqrt{\beta_{N,a}}=x^a\sqrt{\beta_{N,a}}\).
The remaining contraction has diagonal coefficient
\(x^{d-a}g_ax^{-a}=1\), proving the second identity.
The ordinary cap alone is not identified with a Hermitian dual;
the original pivot and both displayed \(N\) factors are essential.

For the negative orientation take
\(\Psi_N^-=\mathsf P\overline{\Psi_N^+}\).
Equivalently it is \(x^d(H_N\otimes I)p/N\), so its additional
factor is a specified unit phase. It gives
\((\Psi_N^-)^*(C\otimes I)\Psi_N^-=\operatorname{Tr}(P_NC)\).
For an actual unmarked one-cut knot operator this is the same
original scalar, by [W]. For arbitrary marked \(C\), its comparison
with the highest cut retains exactly [W]'s finite Ward current.
No new equality of arbitrary marked source probes is assumed.

## 5. Whole purified inputs and the paid tail

Use [W]'s censored trace-one cut at \(m-1\): keep
\(\beta_{N,a}\) for \(a<m-1\), put
\(\sum_{a\ge m-1}\beta_{N,a}\) at \(m-1\), and use zero thereafter.
Let \(\Psi_N^{\pm,[m]}\) be (24) and its negative counterpart
with these censored probabilities. They are unit vectors in
\(H_m^\pm\), with their exact cap/pivot dictionary (25).
The artificial last mass and its Ward current have not been dropped.

If \(t_{N,m}=\sum_{a\ge m}\beta_{N,a}\), elementary square-root
algebra gives
\[
 \|\Psi_N^\pm-\Psi_N^{\pm,[m]}\|^2\le2t_{N,m},\qquad
 t_{N,m}\le C_L(C_L/m)^m .
 \tag{26}
\]
For the first inequality, the last-coordinate difference has square
at most \(t_{N,m}\), and the removed coordinates have total square
\(t_{N,m}\). The second is the actual finite factorial tail in [W],
uniformly for all \(\lambda\in[0,L]\).

Given \(A_0>0\), choose a fixed
\(c>2(\log20+A_0)\) and
\[
                         m_N=\lceil cN/\log N\rceil .
 \tag{27}
\]
For large \(N\), this is at most \(N/2\). The original physical
crossing bound [P], \(\|R_N^\pm\|\le\|R_N^\pm\|_{\rm HS}
\le20^{N-1}\), proves
\[
 \|R_N^\pm(\Psi_N^\pm-\Psi_N^{\pm,[m_N]})\|
 \le e^{(\log20-c/2)N+o(N)}=O(e^{-A_0N}) .
 \tag{28}
\]
In particular this is an absolute error estimate using exact
finite-\(N\) coefficients, not substitution of Poisson weights.
Apply (6) to the censored unit vectors and then (28). It follows
uniformly on every real compact interval \(0\le\lambda\le L\) that
\[
                       \frac1N\log\|R_N^\pm\Psi_N^\pm\|
                                         \longrightarrow h_* .
 \tag{29}
\]
This includes \(\lambda=0\). Positivity of the input probabilities
is used only for the purification and its square-root tail bound;
no positive crossing coefficients or closed period are asserted.

## 6. Relation to earlier endpoint models and source scope

[E] already proves subexponential factorial-chart costs on sublinear
head bands, with the exact Fourier source and endpoint arrows.
[T] proves bounded Euler transitions for compressed single-interval
head blocks in appropriate factorial gauges. It explicitly keeps
the complementary and cross-collar blocks. The present result
estimates the full outgoing high/low column family, including the
bulk reached by long transfers, and controls arbitrary coherent
combinations before taking their norm.

[W]'s trace-class Poisson limit has error \(O(N^{-1})\).
That algebraic error is not multiplied through a growing crossing
here. Only its exact finite censored model is used in (26)--(28).
A complex parameter can be treated by a holomorphic source/co-source
pair on a square-root chart, but no positive Hermitian purification
or uniform nonzero norm theorem for such complex parameters is claimed.

Neither (6) nor (29) supplies a lower bound after a prescribed
ordinary or marked cap. Nor do these estimates assert that arbitrary
turns, branches, or neighboring short components preserve the
selected endpoint spans or the exponent \(h_*\). The returned
source still has its original coherent contraction; its overlap
has not been estimated. In particular this is not a knot-volume
or finite-exception theorem.

## Complete chosen inputs and coverage

All six complete texts below were read at matching versions.
The source identities and methods are credited in the proof;
the endpoint-column, Gram and purified-output estimates are
proved above in the uniform physical metric.

| Label | Complete text | SHA-256 |
| --- | --- | --- |
| G, direct | [Whole physical crossing](research_full_physical_crossing_gaussian_packet.md), 306 lines | 7f1b9932f88aa549bc55088b6f056f5a362548bc51c9fdd7c6b00469e725f531 |
| P, direct | [Original physical source and costs](research_conway_uniform_physical_quartic.md), 477 lines | 39895b430535f565d30133b46ef57f67589207bc83f40597ffe96e2ce79bbda8 |
| C, method coverage | [Selected physical cluster Gram](research_sublinear_physical_casimir_cluster_gram.md), 412 lines | 7cfecc06fdba21757a89abd8e33d630aaccf6a306de1fd6f4f35bbedce6dabdb |
| W, direct | [Actual endpoint cut and censored window](research_trace_class_endpoint_ward_model.md), 404 lines | 6ca7f4eb76ded6cd40ef71c3c2111302f6b7555dccef80dac12fc93b092a8879 |
| E, coverage | [Physical endpoint factorial chart](actual_endpoint_head_factorial_chart.md), 265 lines | 5cea9fc9b738c68e77b8d86b0445d4110df14f614b333032ba87faa98bff1b0c |
| T, coverage | [Compressed actual Euler transition](research_actual_compressed_endpoint_euler_transition.md), 410 lines | 9c735f005fa94afe56931af5fc0cb77ee95849a9c4c89067290711135ad1ed16 |

Only written mathematics, source reads and metadata hashes were used.
No mathematical program, numerical experiment, test, build, git
operation, prior-final edit or public-manuscript change was performed.
