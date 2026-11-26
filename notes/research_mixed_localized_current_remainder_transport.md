# Uniform finite-level remainders for localized three/four currents

Research deduction, 7 November 2026. The operation-preserving
[local phase and amplitude class](research_mixed_actual_prefix_arbitrary_letter_phase_class.md)
also controls a normalized analytic \(O(N^{-1})\) remainder for
iterated **localized exact currents**. The constants are independent
of the preceding word and the next letter. Every finite scalar
normalization and every actual action increment is retained.

There is an exact decomposition of the original finite source into
this local operation and a complementary term. No estimate for that
complementary term is proved here. In particular, the theorem does
not assert that an actual whole cut function is close to its localized
current. The completed prepared-\(34\) Fourier packet is not substituted
for such a retained-leg assertion. No numerical evaluation is used.

## 1. An exact cut function and its finite recurrence

Use the original matrices of
[exact wire contraction](research_mixed_wire_exact_contraction.md).
Write
\[
 r_N=e^{-2\pi i/N},\qquad P_j=(r_N;r_N)_j,\qquad
 \kappa_N=e^{\pi i(N-1)^2/(2N)}.
\tag{1}
\]
Let \(G_N\) be the positive sine-factorial interpolation of
[the exact factorial theorem](exact_factorial_interpolation_and_complex_contours.md),
and define its negative-root marked version by
\[
 \Pi_N(z)=G_N(Nz)
       \exp\!\left\{\frac{\pi i}{2}[N(z-z^2)-z]\right\}.
\tag{2}
\]
It is holomorphic and nonzero on \(0<\Re z<1\), and
\(\Pi_N(j/N)=P_j\) for \(1\le j<N\). Its exact recurrence gives,
where the ratio is regular,
\[
 \frac{\Pi_N(b+j/N)}{\Pi_N(b)}
                   =(r_Ne^{-2\pi ib};r_N)_j.
\tag{3}
\]
The negative-root phase in (2) is part of this definition; it is
not the oppositely marked factorial with its phase suppressed.

For \(0\le j<N\), put
\[
 \Gamma_{j,N}(b)=
 \frac{e^{2\pi ijb}(r_Ne^{-2\pi ib};r_N)_j}
                    {P_j^2\Pi_N(b)}.
\tag{4}
\]
This is one exact holomorphic continuation on the whole open strip.
At \(b=k/N\), \(1\le k<N\), it equals the original
\(\Gamma_{jk}\), including the exact zero when \(j+k\ge N\).
Indeed the finite product then contains \(1-r_N^N\).
At the physical node \(k=0\) we simply retain the original
matrix entry. Nothing below requires an interpolation theorem at
the endpoint of the open strip.

For a nonempty word \(w=(n_1,\ldots,n_m)\) in \(\{3,4\}\), let
\[
 \ell_{w,N}^{\,T}
      =b_N^{\,T}B_{n_1}\Gamma\cdots\Gamma B_{n_m},\qquad
 \mathcal D_{w,N}(b)=\sum_{j=0}^{N-1}(\ell_{w,N})_j
                                      \Gamma_{j,N}(b).
\tag{5}
\]
Here \(b_N=Sv_N(-2)\) is the original complete ordinary boundary
vector, not a new observation. Physical values in (5), including
the separately retained value at zero, are exactly
\(d_{w,N}^{\,T}=\ell_{w,N}^{\,T}\Gamma\).

Consequently the following is an exact identity for complex \(b\)
in the strip:
\[
 \mathcal D_{w(3+\alpha),N}(b)
   =\sum_{\substack{i,j\ge0\\i+j<N}}
       \mathcal D_{w,N}(i/N)(B_{3+\alpha})_{ij}
                                      \Gamma_{j,N}(b),
 \qquad \alpha=0,1.
\tag{6}
\]
The value at \(i=0\) means the original physical datum. Equation (6)
is matrix multiplication followed by (4), not an interpolation of an
arbitrary vector. It retains all physical rows, triangular zeros,
chirps, and original repeated-root information at both parities.

## 2. The localized exact attachment

Use the disks, anchor, and one-form norm of the local class:
\[
\begin{aligned}
 c_3&=.35-.01i,& R_3&=.09,\\
 c_4&=.30-.052i,& R_4&=.064,\\
 \Omega&=\operatorname{int}D_3\cup\operatorname{int}D_4,
 &b^\dagger&=.325-.031i,\\
 \|h\|_*&=\max_{\beta=3,4}\sup_{b\in\operatorname{int}D_\beta}
 R_\beta\left(1-\frac{|b-c_\beta|^2}{R_\beta^2}\right)|h(b)|.
\end{aligned}
\tag{7}
\]
All functions are compatible holomorphic functions on the union.
The actual retained phase is \(H_w\). More generally one may use any
admitted phase \(H=H_w+P_h\), with its action constant kept separately,
from the closed phase ball of the cited theorem. Define
\[
 F(r,t;b)=H(r)+V_\alpha(r,t)+G(t,b),\qquad
 Z(b)=(r_*(b),t_*(b)),\qquad H^+(b)=F(Z(b);b),
\tag{8}
\]
where all primitives have the original lifts. Thus for \(h=0\),
\(H^+=H_{w(3+\alpha)}\) absolutely, including its constant.

The proved image bounds are
\[
 |r_*(b)-c_{3+\alpha}|<
 \begin{cases}.084,&\alpha=0,\\ .061,&\alpha=1,
 \end{cases}
 \qquad b\in D_3\cup D_4.
\tag{9}
\]
The reduced negative Hessian has a common accretivity floor
\(7\mu/8\), where \(\mu=6\pi/49\). The unperturbed floor is
\(\mu\). These are complex Schur bounds of the original full
Hessian, not bounds on a different polarization.

There are a single \(a>0\) and a single \(\tau>0\), independent of
the word, letter, and admitted phase, with the following properties.
The roots and the phase (8) extend compatibly to the union
\(\Omega_\tau\) of the disks enlarged by \(\tau\). On that union the
translated box
\[
                    Z(b)+[-a,a]^2
\tag{10}
\]
and a fixed complex neighborhood of it lie in the original regular
factorial domain. Every input \(r\) used in this neighborhood lies
in a fixed compact subset of \(\Omega\). The horizontal descent obeys
\[
 \Re\{F(Z(b)+u;b)-H^+(b)\}\le-c|u|^2
                 \quad(u\in[-a,a]^2)
\tag{11}
\]
for one \(c>0\).

Here uniformity does not require a bound for \(H_w\)'s additive
constant or for a Bloch-type input at the outer disk boundary.
The local-class proof bounds \(H_w'\) uniformly on the typed disks;
Cauchy gives all its fixed higher derivatives on smaller disks.
It bounds \(h\) and its fixed derivatives on the strict inner image
domains in the same way. The inverse of the two-dimensional Hessian
and every boundary coupling are uniformly bounded. A fixed-size
Newton/implicit-function argument therefore extends \(Z\) a common
distance in \(b\), with its input still strictly inside \(\Omega\).
Uniqueness glues the extensions on overlaps. Shrinking \(a,\tau\)
retains a positive accretivity floor on (10), which proves (11) by
integration from the stationary point. For example all input
neighborhoods can be chosen inside the disks of radii \(.086,.063\),
with further fixed buffers still inside \(R_3,R_4\). All constants
are existence constants from these fixed compact domains; no new
function values are needed.

On the regular domain define the exact central row
\[
 K_{\alpha,N}(r,t;b)=\kappa_N^{1+\alpha}N^\alpha e^{2\pi iNtb}
 \frac{\Pi_N(r+t)\Pi_N(t+b)}
      {\Pi_N(r)^\alpha\Pi_N(t)^{\alpha+2}\Pi_N(b)^2}.
\tag{12}
\]
It is the literal interpolation of \(B_{3+\alpha}\Gamma\) there.
The factorial theorem, including its uniform first correction, gives
\[
\begin{split}
 K_{\alpha,N}(r,t;b)
  &=\kappa_N^{1+\alpha}N^{-1}
         e^{N[V_\alpha(r,t)+G(t,b)]}k_{\alpha,N}(r,t;b),\\
 k_{\alpha,N}&=k_\alpha+O(N^{-1}),\\
 k_\alpha(r,t;b)
  &=\frac{\mathfrak a(r+t)\mathfrak a(t+b)}
       {\mathfrak a(r)^\alpha\mathfrak a(t)^{\alpha+2}
        \mathfrak a(b)^2},\qquad
 \mathfrak a(z)=\sqrt{2\sin\pi z}\,e^{-i\pi z/2}.
\end{split}
\tag{13}
\]
The error and every fixed derivative are uniform on those fixed
compact domains. In particular this uses an actual \(O(N^{-1})\)
factorial expansion, not an arbitrary-rate-tolerance estimate.

For a holomorphic input \(C\) on \(\Omega\), the localized exact
operator is
\[
 (\mathcal L_{w,\alpha,N}C)(b)
       =N^2\int_{[-a,a]^2}C(r_*(b)+u_1)
                K_{\alpha,N}(Z(b)+u;b)\,du_1du_2.
\tag{14}
\]
It only uses \(C\) in the strict inner input domain. The moving box
is parametrized by fixed real \(u\), so (14) is holomorphic in \(b\).
It is an exact integral of the original local row; it is not asserted
to equal the full discrete operation (6).

## 3. A uniform analytic stationary operator estimate

For a holomorphic amplitude \(A\) on the inner input domain, put
\[
 (T_NA)(b)=N\int_{[-a,a]^2} A(r_*(b)+u_1)
       k_{\alpha,N}(Z(b)+u;b)
       e^{N[F(Z(b)+u;b)-H^+(b)]}\,du.
\tag{15}
\]
Let
\[
 m(b)=\frac{2\pi k_\alpha(Z(b);b)}
                {\sqrt{\det[-F_{(r,t)(r,t)}(Z(b);b)]}}.
\tag{16}
\]
The square root is the original oriented accretive Gaussian branch.
The local class proves uniform upper and nonzero lower bounds for
\(m\), and bounds its logarithmic derivative in (7).

**Lemma 1.** There is a fixed compact input domain \(K\Subset\Omega\),
with a fixed surrounding complex buffer, and a constant \(C\) such that
\[
 T_NA=m\,A\circ r_*+\mathcal E_NA,
 \qquad
 \|\mathcal E_NA\|_{C^1(\overline\Omega)}
                     \le\frac C N\sup_K|A|.
\tag{17}
\]
In this formula the surrounding buffer is included in \(K\), so its
supremum controls the derivatives used in the proof. The operator
\(\mathcal E_N\) is linear. Constants are uniform over all preceding
words, both letters, and the admitted phase ball. The same conclusion
holds for any fixed number of output derivatives, with its own constant.

*Proof.* The corresponding supremum estimate holds first on a common
slightly enlarged output domain, by the domain argument preceding
(12). Uniform Cauchy estimates bound all needed input derivatives
by \(\sup_K|A|\). On the symmetric central box
\(|u_j|\le N^{-2/5}\), expand the phase through fourth order and
the amplitude through second order and set \(u=v/\sqrt N\).
The term of order \(N^{-1/2}\) is an odd polynomial times the even
complex Gaussian, so its integral on a symmetric box vanishes.
The fourth-order phase term, square of the cubic term, second-order
amplitude term, and mixed terms are bounded by \(C/N\) times
Gaussian moments. Taylor remainders have the same or smaller bound,
using (11) and fixed higher derivatives. The rest of (10) has bound
\(Ce^{-cN^{1/5}}\sup_K|A|\); replacing the central Gaussian box
by \(\mathbb R^2\) makes an error of that order as well.
The exact \(k_{\alpha,N}-k_\alpha\) term contributes \(C/N\)
by (13). The Gaussian integral is exactly (16). This proves the
supremum estimate. Cauchy between the enlarged output domain and
\(\overline\Omega\) proves (17) and its fixed-derivative versions.
Every domain buffer and derivative bound was chosen independently
of the word. \(\square\)

The preceding proof is an operator estimate, not merely an asymptotic
for a single fixed amplitude. This distinction supplies the Lipschitz
bound for remainders below.

## 4. An invariant \(O(N^{-1})\) remainder ball

Let \(f=e^\ell\) be a leading amplitude in the established invariant
class, normalized by \(\ell(b^\dagger)=0\) and
\(\|\ell'\|_*\le M\). Consider the localized input
\[
 C_N(b)=c_N N^{-3/2}e^{NH(b)}f(b)e^{e_N(b)},\qquad
 e_N(b^\dagger)=0.
\tag{18}
\]
The nonzero scalar \(c_N\) is retained exactly. It includes all
previous carriers and finite normalizations. No bounded supremum
of \(f\) or \(e_N\) on the entire open union is assumed.

Fix a finite \(u_0>0\) and allow \(\|e'\|_*\le u_0\).
Integrating along the fixed anchor-to-center-to-input paths bounds
\(\ell,e\) uniformly on \(K\), including its buffers. Thus \(fe^e\)
and its reciprocal are uniformly bounded there. The same is true on
the extended critical input images used for output Cauchy estimates.
Lemma 1 gives
\[
 T_N(fe^e)(b)=m(b)f(r_*(b))e^{e(r_*(b))}
                                  [1+\delta_N(e;b)].
\tag{19}
\]
For \(N\) sufficiently large, uniformly in the stated classes,
\[
\begin{split}
 \|\delta_N(e)\|_{C^1(\overline\Omega)}&\le C/N,\\
 \|\delta_N(e_1)-\delta_N(e_2)\|_{C^1(\overline\Omega)}
          &\le(C/N)\|(e_1-e_2)'\|_* .
\end{split}
\tag{20}
\]
For the second inequality use linearity of \(\mathcal E_N\), the
uniform nonzero denominator in (19), and
\(\sup_K|e_1-e_2|\le C\|(e_1-e_2)'\|_*\).
The last bound uses their common zero at the anchor. These estimates
first hold on the slightly enlarged output domain; Cauchy gives the
displayed derivative bounds. They do not use a supremum at the
boundary of the input disks.

Let \(q_N(e;b)=\log[1+\delta_N(e;b)]\), with the branch near zero.
After increasing \(C\), (20) holds for \(q_N\) also. The exact output
of (14) has the form (18), with phase \(H^+\), leading amplitude
\[
 f^+(b)=\frac{m(b)f(r_*(b))}
                  {m(b^\dagger)f(r_*(b^\dagger))},
 \qquad \mu=m(b^\dagger)f(r_*(b^\dagger)),
\tag{21}
\]
and exact updates
\[
\begin{split}
 e^+(b)&=e(r_*(b))-e(r_*(b^\dagger))
                   +q_N(e;b)-q_N(e;b^\dagger),\\
 c_N^+&=c_N\kappa_N^{1+\alpha}\mu_N,\\
 \mu_N&=\mu\exp\{e(r_*(b^\dagger))+q_N(e;b^\dagger)\}\ne0.
\end{split}
\tag{22}
\]
All action constants reside in \(H^+\), exactly as in (8).
If normalized phases are used instead, their exact action increment
is transferred to \(c_N^+\) by its literal exponential. No bulk action
or classical scalar is substituted.

**Theorem 2.** For a uniform constant \(C\), the normalized remainder
operation satisfies
\[
\begin{split}
 \|(e^+)'\|_*&\le\lambda\|e'\|_*+C/N,\\
 \|(e_1^+-e_2^+)'\|_*&\le(\lambda+C/N)
                                      \|(e_1-e_2)'\|_*,
 \qquad \lambda=61/64.
\end{split}
\tag{23}
\]
There exist \(K,N_0\), independent of the word and next letter,
such that the ball \(\|e'\|_*\le K/N\), \(e(b^\dagger)=0\),
is invariant for every \(N\ge N_0\). On that ball the operation is
a contraction with constant at most \(125/128\).

*Proof.* The exact Schwarz--Pick estimate of the local-class theorem
gives
\[
              \|(e\circ r_*)'\|_*\le(61/64)\|e'\|_*.
\tag{24}
\]
Combine this with (20)--(22); the radius factors in (7) are retained.
Choose \(K\ge128C/3\), and then \(N_0\) so that \(K/N_0\le u_0\)
and \(C/N_0\le3/128\). The first line of (23) preserves the ball,
and the second gives \(122/128+3/128=125/128\).
\(\square\)

The estimate also gives a bounded normalized relative error on the
whole union after each attachment. Both values of \(e\circ r_*\)
in (22) are evaluated on strict inner images, whose anchor paths
have weighted length less than three. Therefore
\[
 \sup_\Omega |e^+|\le6K/N+2C/N,
 \qquad \mu_N/\mu=1+O(N^{-1}).
\tag{25}
\]
The multiplier bounds are uniform and nonzero. Every fixed derivative
of the normalized relative error is \(O(N^{-1})\) on any fixed smaller
output domain, by Cauchy. The exact finite scalars in (22) are essential:
after \(j\) attachments their ratio to the product of the leading
scalars is only bounded by \(\exp(O(j/N))\). No uniform replacement
of that product by its classical value is asserted for arbitrary \(j\).

## 5. Actual local seeds and arbitrary localized sequences

There are two actual one-letter localized seeds. Use the original
complete coefficient \(b_N(s)=D_N(s)^{-1}C_N(s)\), rather than a
terminating formula valid only at physical nodes, in the local
two-index integral for \(b_N^TB_{3+\alpha}\Gamma\).
The full endpoint packet used in
[the literal prefix source theorem](research_mixed_fourier_prefix_local_current.md)
holds on a neighborhood of every resulting private-index image.
The endpoint maps put those images strictly in \(E_{\rm cap}\) for
both external typed disks. Its symbol, the factorial symbols, and the
reduced Gaussian coefficient are holomorphic and nonzero there.

Choose the two seed boxes small enough for the same translated-box
construction on neighborhoods of both closed output disks. These are
only two fixed cases. Their exact localized integrals have normalized
remainders with \(\|e_{0,N}'\|_*\le C_0/N\), and a uniform supremum
bound \(C_0/N\), by the actual endpoint packet and Lemma 1's argument.
Choose \(K\) also at least \(C_0\). This is a statement about the
localized seed integrals; their entire discrete cut functions are not
being estimated by this argument.

Starting with either seed and using (14) for an arbitrary sequence of
letters, Theorem 2 proves, for all \(N\ge N_0\),
\[
 C_{w,N}(b)=c_{w,N}N^{-3/2}e^{NH_w(b)}f_w(b)
                                      [1+O(N^{-1})]
\tag{26}
\]
uniformly on \(\Omega\), with fixed derivatives on smaller domains.
Here \(c_{w,N}\ne0\) is the seed scalar times the **exact**
normalizations (22), \(f_w\) is the normalized original leading amplitude, and
the constant in the normalized error is independent of the word
length and order. The actual phases have error zero; the same local
operator theorem applies to an admitted perturbed phase orbit.

Equation (26) concerns the explicitly iterated localized integrals.
Their leading phases and symbols are those of the original word by
stationary elimination and Gaussian Schur associativity. It does
not identify these iterated local cycles with the entire original
finite sum. The cut power remains \(N^{-3/2}\): the new exact row has
power \(N^{-1}\), two indices supply \(N^2\), and their Gaussian
supplies \(N^{-1}\). Each letter also retains
\(\kappa_N^{1+\alpha}\). Both parities and the original branches
are unchanged.

## 6. The exact unpaid exterior term

For clarity, the full actual recurrence and the localized theorem
can be joined without defining a localized current at unrelated
physical nodes. Define
\[
 \mathcal B_{w,\alpha,N}[\mathcal D_w](b)
 :=\sum_{\substack{i,j\ge0\\i+j<N}}
 \mathcal D_w(i/N)(B_{3+\alpha})_{ij}\Gamma_{j,N}(b)
                  -(\mathcal L_{w,\alpha,N}\mathcal D_w)(b).
\tag{27}
\]
All physical data in the sum are actual data, with the zero node
retained separately. The local integral uses the actual holomorphic
cut function (5) only where it is defined in the strip.

Equation (27) also has the original source-contour interpretation.
Choose a fixed central real rectangle containing all new critical
real coordinates strictly in its interior, for example
\([.23,.45]^2\), with lattice-avoiding boundary shifts of size
\(O(N^{-1})\) when needed. Its closure lies inside \(r+t<1\), and
\(t+b\) has real part strictly below one for \(b\in D_3\cup D_4\).
On its complex tube the ratio (3) turns the actual row into (12).
Apply the exact cotangent residue identity to the central lattice
rows, keeping the rest of the original supported rows as physical
rows. Deform the zero-frequency central current to its critical
heights and separate (10). The resulting remainder consists of all
outer physical rows, nonzero Fourier alternatives, vertical sides,
support-boundary contributions where present, zero-frequency joining
pieces, and the rest of the central sheet. Their signs and orientations
are the original ones. This description makes no bound for their
absolute values. Equivalently (27), which needs no contour choice,
defines their exact total.

Let \(C_{w,N}\) be the iterated localized current and define only
on \(\Omega\)
\[
                  R_{w,N}=\mathcal D_{w,N}-C_{w,N}.
\tag{28}
\]
Linearity of the local operator and (6), (27) give the exact identity
\[
 R_{w(3+\alpha),N}
     =\mathcal L_{w,\alpha,N}R_{w,N}
          +\mathcal B_{w,\alpha,N}[\mathcal D_{w,N}].
\tag{29}
\]
The localized current is never sampled outside \(\Omega\).
Neither is \(R_{w,N}\): its occurrence in (29) is only inside the
strict local input domain. The complementary term uses the complete
actual source, including all physical rows outside that domain.

Thus the new uniform estimate controls the normalized finite-level
error generated by repeated **local** attachments. To infer an
actual-source induction one must still control the seed difference
(28) and the transported complementary source (27) in the required
original closing or boundary norm. No such smallness is assumed or
proved here. In particular neither a local Fourier packet nor the
global prepared-\(34\) Fourier profile weight is identified with a
retained cut norm. The source-germ and turn distinction in
[the original remainder obstruction](research_source_germ_truncation_and_turn_remainders.md)
therefore remains intact.
