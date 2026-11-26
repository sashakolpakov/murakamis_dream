# Real-meridian transport and one form for every meridian jet

Written research proof, 23 November 2026. The original complete-head
Hermitian form extends to the actual root meridian family on positive
real meridians. The full original mixed-color crossing, including its
unrolled Cartan diagonal, preserves it. Holomorphic polarization then
gives all meridian derivative identities at once. A finite packet of
meridian jets has an explicit nondegenerate Hermitian form preserved
by the truncated original word.

The forms are indefinite. The result removes repeated meridian-jet
adjoint calculations; it does not bound a marked closing below, reduce
the physical dimension to a fixed number, or concern derivatives of
the quantum parameter away from its root.

## 1. The actual root meridian family

Fix
\[
 N\geq2,\quad d=N-1,\quad q=e^{\pi i/N},\quad Q=q^2,
 \quad F_h=(Q;Q)_h .                                      \tag{1}
\]
The quantum parameter stays fixed throughout. On each original balanced
head use the physical basis \(|a\rangle\), \(0\leq a\leq d\), and
\[
 \begin{gathered}
 x=-q^{-1}M,\qquad
 \alpha(M)=d+\frac{N}{\pi i}\Log M,\qquad q^{\alpha(M)}=x,\\
 K_x|a\rangle=xQ^{-a}|a\rangle,\qquad
 \mathsf h_\alpha|a\rangle=(\alpha-2a)|a\rangle,\\
 f|a\rangle=(1-Q^{a+1})|a+1\rangle\quad(a<d),\qquad f|d\rangle=0,\\
 e_x|a\rangle=(x^{-1}-QxQ^{-a})|a-1\rangle\quad(a>0),
 \qquad e_x|0\rangle=0 .
 \end{gathered}                                                  \tag{2}
\]
These are the original matrices of [A,E]; the zero endpoint in \(e_x\)
is part of the module. It is not replaced by a cyclic arrow.
The branch \(\Log M\) is real for \(M>0\), continued from that branch
when a complex meridian germ is used. In particular \(\alpha(1)=d\).

Define the same one-head physical form at every meridian:
\[
 Z|a\rangle=Q^a|a\rangle,\qquad R_d|a\rangle=|d-a\rangle,
 \qquad H_N=q^{-1}Z^{-1}R_d .                            \tag{3}
\]
Thus \(H_N|a\rangle=qQ^a|d-a\rangle\),
\(H_N^\dagger=H_N\), and \(H_N^2=I\).
Write \(A^\sharp=H_NA^\dagger H_N\) on one head, and use the
corresponding tensor form on several heads.

For positive real \(M\), \(\bar x=Qx\) and
\(\bar\alpha=2d-\alpha\). Direct substitution in (2) proves
\[
 K_x^\sharp=K_x,\qquad e_x^\sharp=e_x,\qquad
 f^\sharp=Q^{-1}f,\qquad
 \mathsf h_\alpha^\sharp=-\mathsf h_\alpha .            \tag{4}
\]
For example, on input \(a>0\), the coefficient of
\(H_Ne_x^\dagger H_N\) is
\(Q[Q^{-1}x^{-1}-xQ^{-a}]=x^{-1}-QxQ^{-a}\).
On input \(a=0\), the actual top zero of \(e_x^\dagger\) gives zero.
Similarly the coefficient for \(H_Nf^\dagger H_N\) is
\(Q^{-1}(1-Q^{a+1})\), including its top zero.
For \(\mathsf h_\alpha\), reflection of \(a\) gives
\(\bar\alpha-2(d-a)=-\alpha+2a\).

These identities are compatible with the actual coproducts
\[
 \Delta e=e_1K_2+e_2,\qquad
 \Delta f=f_1+K_1^{-1}f_2,\qquad
 \Delta K=K_1K_2,\qquad
 \Delta\mathsf h=\mathsf h_1+\mathsf h_2 .              \tag{5}
\]
For instance \((\Delta e)^\sharp=\Delta e\) and
\((\Delta f)^\sharp=Q^{-1}\Delta f\). Distinct tensor factors
commute in these calculations. No positive real form is asserted:
the nonzero nilpotent \(e_x\) is self-adjoint for an indefinite form.

## 2. Full original crossings, with their unrolled diagonal

Use the actual finite preflip factorization of [A, Section 2],
with the original unstripped universal Cartan normalization
explicit in [C, (5)] and retained as in [E]:
\[
 \begin{gathered}
 R_0(M_1,M_2)=D_{12}P_N(e_{x_1}f_2),\qquad
 D_{12}=q^{\mathsf h_{\alpha_1}\mathsf h_{\alpha_2}/2},\\
 D_{12}|a,b\rangle
   =\exp\!\left\{\frac{\pi i}{2N}
                 (\alpha_1-2a)(\alpha_2-2b)\right\}|a,b\rangle,\\
 P_N(Y)=\sum_{h=0}^d
        \frac{(-1)^hQ^{h(h-1)/2}}{F_h}Y^h .
 \end{gathered}                                                  \tag{6}
\]
Indeed \(e=q\rho^2E\), with \(\rho=q-q^{-1}\), and
\(F_h=(-1)^hq^{h(h+1)/2}\rho^h[h]_q!\). Substitution converts the
original universal coefficient in [C, (5)] exactly into that of
\(P_N(e_{x_1}f_2)\); it introduces no additional scalar.
Its checked version is \(\check R(M_1,M_2)=\mathsf P R_0(M_1,M_2)\),
where \(\mathsf P\) is the literal flip from input colors
\((M_1,M_2)\) to output colors \((M_2,M_1)\).
In particular the highest entry
\(\kappa=q^{\alpha_1\alpha_2/2}\) has not been removed.
Away from completeness this separate scalar need not have modulus one.

The nilpotent argument \(Y=e_{x_1}f_2\) satisfies \(Y^N=0\).
From (4), \(Y^\sharp=Q^{-1}Y\). The elementary factorial conjugation
and finite Euler inverse are
\[
 \overline{F_h}=(-1)^hQ^{-h(h+1)/2}F_h,\qquad
 P_N(Y)^{-1}=\sum_{h=0}^dY^h/F_h .                     \tag{7}
\]
The inverse follows coefficientwise below degree \(N\) from the finite
\(Q\)-binomial identity; larger powers vanish. Hence
\[
 P_N(Y)^\sharp=\sum_{h=0}^dY^h/F_h=P_N(Y)^{-1}.
 \tag{8}
\]
No factor \(F_N\) occurs. For the original full Cartan factor, (4) gives
\((\mathsf h_{\alpha_1}\mathsf h_{\alpha_2})^\sharp
=\mathsf h_{\alpha_1}\mathsf h_{\alpha_2}\). Conjugating the coefficient
\(\pi i/(2N)\) in (6) therefore proves
\[
 D_{12}^\sharp=D_{12}^{-1},\qquad
 R_0^\sharp=P_N(Y)^{-1}D_{12}^{-1}=R_0^{-1}.
 \tag{9}
\]
This uses the full unrolled diagonal, not an absolute-value estimate on
\(\kappa\). Since the flip is an isometry between the two identical
tensor forms, the checked crossing satisfies
\[
 \boxed{\quad
 \check R(M_1,M_2)^\dagger(H_N\otimes H_N)
           \check R(M_1,M_2)=H_N\otimes H_N
 \quad(M_1,M_2>0).\quad}                               \tag{10}
\]
Its genuinely typed negative crossing is the corresponding inverse.
When a negative crossing starts with unequal colors \((M_1,M_2)\),
that inverse is taken from the positive map with input colors
\((M_2,M_1)\). No exchange of these source and target orders is implicit.

For a signed colored word \(\mathcal W_\omega(\boldsymbol M)\) of
width \(b\), label meridians on the initial strands and carry them
through its actual crossing permutation. Put \(\mathscr H_b=H_N^{\otimes b}\).
Successive applications of (10), including overlapping adjacent pairs,
give
\[
 \mathcal W_\omega(\boldsymbol M)^\dagger\mathscr H_b
                  \mathcal W_\omega(\boldsymbol M)=\mathscr H_b,
 \qquad \boldsymbol M\in(0,\infty)^b .                 \tag{11}
\]
Every original crossing scalar is included. The number of crossings,
their signs and both level parities cause no exception.

## 3. Polarization and all derivative Wronskians

Choose a positive real meridian tuple \(\boldsymbol M^0\), and use
the logarithmic coordinates
\(M_i=M_i^0e^{t_i}\) on a small conjugation-invariant polydisc.
Let \(W(t)=\mathcal W_\omega(\boldsymbol M^0e^t)\).
It is the actual holomorphic matrix germ with its original unrolled
branches. Define the holomorphic reflected transpose
\[
 W^\natural(t)=\overline{W(\bar t)}^{\mathsf T}.
 \tag{12}
\]
Equation (11) holds on its real slice. The identity theorem, applied
one coordinate at a time to that real open box, therefore yields
\[
 \boxed{\qquad W^\natural(t)\mathscr H_bW(t)=\mathscr H_b.
 \qquad}                                               \tag{13}
\]
This is an identity of full meridian germs. Reflection conjugates the
continued logarithmic branches; unrelated windings are not identified.

For a multi-index \(\alpha\), put
\(D_i=M_i\partial_{M_i}\) and \(D^\alpha=\prod_iD_i^{\alpha_i}\).
Differentiating (13) at the positive real tuple gives every mixed
meridian derivative identity in one formula:
\[
 \boxed{\quad
 \sum_{\beta\leq\alpha}\binom{\alpha}{\beta}
   (D^\beta\mathcal W_\omega(\boldsymbol M^0))^\dagger
   \mathscr H_b
   D^{\alpha-\beta}\mathcal W_\omega(\boldsymbol M^0)
 =\begin{cases}\mathscr H_b,&\alpha=0,\\0,&\alpha\ne0.
   \end{cases}\quad}                                   \tag{14}
\]
Equivalently one may replace every
\(D^\gamma\mathcal W_\omega(\boldsymbol M^0)\) by
\(\partial_t^\gamma W(0)\).
The first-order identity is the usual vanishing of
\(W^\dagger\mathscr H_bD_iW+(D_iW)^\dagger\mathscr H_bW\).
Higher identities retain all mixed derivative cross terms.
They are exact at every finite order, not asymptotic estimates.

The same germ identity also retains actual two-fiber transports.
Where the specified continued logarithmic lifts are defined, put
\(T_\delta(t)=W(t+\delta)W(t)^{-1}\). Substituting (13) at the two
arguments, in the displayed order, gives
\[
 T_{\bar\delta}(\bar t)^\dagger\mathscr H_bT_\delta(t)
                                  =\mathscr H_b .       \tag{14a}
\]
For a meridian shift \(M\mapsto q^jM\), \(\delta=j\pi i/N\),
so the paired shift is \(-\delta\). This is the original uncontracted
transport of [E, (9a)], with its logarithmic lifts retained. It does
not say that one such imaginary-shift matrix is an isometry by itself,
or identify a closed quantum-A companion with this full matrix.

## 4. An explicit nondegenerate form on finite meridian jets

Fix nonnegative truncation orders \(r_1,\ldots,r_b\) and set
\[
 A_{\boldsymbol r}=\mathbb C[t_1,\ldots,t_b]/
                 (t_1^{r_1+1},\ldots,t_b^{r_b+1}).
 \tag{15}
\]
Its involution conjugates coefficients and fixes the formal variables.
For physical jet packets \(u,v\in A_{\boldsymbol r}\otimes\mathbb C^{N^b}\),
define
\[
 [u,v]_{\boldsymbol r}
    =[t_1^{r_1}\cdots t_b^{r_b}]
                          u(t)^*\mathscr H_bv(t).
 \tag{16}
\]
Here the star on a formal vector means coefficientwise conjugate
transpose with the same formal variables, not substitution of \(\bar t\).
The matrix of (16) is explicitly
\[
 J_{r_1}^{\rm jet}\otimes\cdots\otimes J_{r_b}^{\rm jet}
                         \otimes\mathscr H_b,
 \qquad (J_r^{\rm jet})_{ij}=\delta_{i+j,r},\quad0\leq i,j\leq r.
 \tag{17}
\]
Thus it is Hermitian and nondegenerate. Every chosen derivative
coefficient and every physical head coordinate remains present;
no additional radical quotient is taken.
Its matrix squares to the identity, so all its singular values are
one. This is a statement about this indefinite coefficient pairing,
not a positive norm estimate or a condition-number bound for a word.

Let \(W_{\boldsymbol r}\) be multiplication by the Taylor polynomial
of \(W(t)\) in this jet algebra. Equation (13) implies its exact
truncated coefficient identity, and hence
\[
 [W_{\boldsymbol r}u,W_{\boldsymbol r}v]_{\boldsymbol r}
                              =[u,v]_{\boldsymbol r}.
 \tag{18}
\]
Indeed substitute \(W(t)u(t),W(t)v(t)\) into (16), use (13), and
extract the top coefficient. Terms killed by (15) cannot affect it.
The jet map is invertible since its constant coefficient is invertible.
For one parameter and first jets its matrix is
\(\left(\begin{smallmatrix}W_0&0\\W_1&W_0\end{smallmatrix}\right)\),
and its form is
\(\left(\begin{smallmatrix}0&\mathscr H_b\\\mathscr H_b&0\end{smallmatrix}\right)\).
Thus (18) simultaneously contains the zeroth- and first-order identities.

## 5. Original boundary observations and scope

The adjoint used here is not an unrecorded change of Hopf dual or of
head order. The original antipodes remain
\(\mathscr S(K)=K^{-1}\), \(\mathscr S(e)=-eK^{-1}\),
\(\mathscr S(f)=-Kf\), with their original left/right placements.
For example, a genuine linear dual reverses the weights and has
\[
 \alpha^\vee=2d-\alpha,\qquad
 x^\vee=Q^{-1}x^{-1},\qquad M^\vee=M^{-1}.
 \tag{19}
\]
This follows from the reversed spectrum of \(-\mathsf h_\alpha\).
It is different from the anti-linear reflection used in (12).
No linear dual color is silently replaced by the same meridian.

For any prescribed original meridian-dependent source \(p(t)\) and
row \(\Lambda(t)\), its scalar and all its retained jets are still
the coefficients of \(\Lambda(t)W(t)p(t)\). The original marked cap,
ordinary turns, pivots, modified dimension and framing/peripheral
lines are kept in these boundary data. Equations (13)--(18) do not
replace \(\Lambda\) by the adjoint of \(p\). At the complete point
the ordinary cup is isotropic for the tensor form, whereas the
original marked cup/cap pairing is one; directly use [A, (18)] and
\(\sum_{a=0}^dQ^a=0\) for the former. These are distinct observations.
No original closing or pivot is declared to be a metric isometry.

This gives one exact orthogonality calculation for all meridian jet
orders and arbitrary signed overlapping words. It avoids constructing
and checking a separate derivative pairing at each order. The jet
dimension is still \(N^b\prod_i(r_i+1)\). Neither fixed jet order nor
the fixed degree of an auxiliary variational formulation makes the
physical boundary dimension independent of \(N\).
There is no positive jet norm, general marked scalar lower bound,
geometric principal-symbol nonvanishing theorem, or estimate for
derivative order growing with \(N\) here. In particular the parameter
\(q\) was never varied: moving-\(q\) normal jets are not meridian jets,
and [E, Section 7] explicitly warns against identifying them.

## Complete proof sources

- [A] [Actual shared quantum flags and their charged exchange](actual_shared_quantum_flags_and_charged_exchange.md), 459 lines, SHA-256 `dcab795cc141e2e1db726998cf7b1141dd03c681eaae9076387f90581f53a7d9`.
- [E] [Actual crossing Euler completion and weight source](actual_crossing_euler_completion_and_weight_source.md), 350 lines, SHA-256 `e3a82ec13787d64a20694c0281337dfd3a5ea1f23ddad800073ed60a82477d89`.
- [C] [Original full half-Cartan and head dilation](actual_half_clock_source_dilation.md), 249 lines, SHA-256 `5f76e05c3130ef482d315681feaca8ecf98c4cc367623ffa72a19316a7706a3f`.

The complete-color [physical tensor-form proof](research_physical_tensor_krein_crossing_form.md),
286 lines, SHA-256 `610b5ac7d889429163ec230e9d644d174d38382733dbad57826fce66cec8e348`,
is coverage only. The proof here works directly with the actual
generic-meridian matrices and full unrolled diagonal, without using
its complete-only flag frame or dropping the original Cartan line.
