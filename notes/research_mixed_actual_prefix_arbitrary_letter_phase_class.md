# A local phase and leading-amplitude class for arbitrary three/four words

Research extension, 7 November 2026. The actual retained-leg phases
admit either single-letter attachment, not only a \(34\) pair.
Throughout this note, a word is a finite sequence of the letters \(3\)
and \(4\), specifying the two original block types.
A common neighborhood contracts by \(61/64\) in a two-disk
holomorphic one-form norm. The compatible local leading amplitudes
also form an invariant class. The original cap, action constants,
symbols, scalar powers and logarithmic lifts remain fixed.

This is a local stationary-phase theorem. Its norm is a norm of
holomorphic phase gradients, not a norm estimate for the full finite
source. No complementary source integral, Fourier seam domain, or
knot statement follows. The earlier
[reviewed \(34\) phase theorem](research_mixed_actual_prefix_finite_step_phase_transport.md)
is unchanged. No numerical evaluation is used.

## 1. The common retained chart

Use its original \(E,V_\alpha,G,\mathcal A_w\), and set
\[
\begin{split}
 D_\nu&=\{|b-c_\nu|\le R_\nu\},\\
 c_3&=.35-.01i,\quad R_3=.09,\qquad
 c_4=.30-.052i,\quad R_4=.064,\\
 \Omega&=\operatorname{int}D_3\cup\operatorname{int}D_4,\qquad
 b^\dagger=(c_3+c_4)/2=.325-.031i,\qquad \mu=6\pi/49.
\end{split}                                                     \tag{1}
\]
For every nonempty positive word \(w\), retain
\[
 \mathcal A_w(z;b)
 =E(s_1,u)+\sum_jV_{\epsilon_j}(s_j,t_j)
    +\sum_{j<m}G(t_j,s_{j+1})+G(t_m,b),\qquad
 H_w(b)=\operatorname{stat}_z\mathcal A_w(z;b).                 \tag{2}
\]
Lemma 1 of
[actual cap-phase entrance](research_mixed_alternating_cap_phase_entrance.md)
explicitly allows either external typed disk in (1), for every
word and every length including one. The same original endpoint
maps and full bidisk maps therefore supply \(z_w(b)\) on both
closed disks. No new existence theorem on an unverified input
domain is assumed.

The two definitions agree on their overlap. They solve the same
original logarithmic equations in the same larger convex
\(U\times E\times Q^{2m-1}\) product, whose gradient is injective.
Their roots coincide, and evaluating the identical unreduced
action makes their values coincide, not merely up to a constant.
Holomorphic continuation and uniqueness glue them near both
closed disks. Hence \(H_w\) is one holomorphic function on
\(\Omega\).

The disks have nonempty intersection containing \(b^\dagger\).
In fact
\[
 |b^\dagger-c_\nu|^2=533/500000<1/900<R_4^2\le R_\nu^2.
                                                               \tag{3}
\]
Their union is star-shaped about \(b^\dagger\), since each disk
is convex and contains that point. In particular \(\Omega\)
is simply connected. A compatible holomorphic gradient error
means one function on this union; two unrelated functions on
the disks are not admitted.

The full retained-leg Schur proof in the previous theorem applies
unchanged for \(b\) in either disk, since both lie in \(Q\).
It gives
\[
             -\Re\mathcal A_w''(z;b)\succ\mu I,\qquad
             -\Re H_w''(b)>\mu.                              \tag{4}
\]
The first inequality includes the external \(b\)-coordinate.
Uniform bounds on \(H_w'\) and \(H_w''\) follow from
\[
 H_w'=G_b(t_m(b),b),\qquad
 H_w''=\mathcal A_{bb}
      -\mathcal A_{bz}\mathcal A_{zz}^{-1}\mathcal A_{zb}.        \tag{5}
\]
The off-diagonal vectors have one entry, the inverse norm is at
most \(1/\mu\), and every primitive belongs to one fixed compact
regular strip. All fixed derivatives of \(H_w'\) are consequently
bounded uniformly on fixed smaller disks. The value
\(H_w(b^\dagger)\) is retained separately.

## 2. Exact attachment and a common perturbation radius

For \(\alpha=0,1\), define
\[
 \mathscr T_\alpha[H](b)
   =\operatorname{stat}_{r,t}
             [H(r)+V_\alpha(r,t)+G(t,b)] .                    \tag{6}
\]
The actual source gives the absolute identity
\[
                  \mathscr T_\alpha[H_w]=H_{w(3+\alpha)} .
                                                               \tag{7}
\]
Indeed one first eliminates the old variables in the original
action of the longer word. The remaining two-variable negative
Hessian is its complex Schur complement, with floor \(\mu\).
At the finite level the exact identity is
\[
 d_{w(3+\alpha),N}^{\,T}
        =d_{w,N}^{\,T}B_{3+\alpha,N}\Gamma_N,\qquad
 d_{w,N}^{\,T}
        =b_N^TB_{n_1}\Gamma_N\cdots B_{n_m}\Gamma_N.             \tag{8}
\]
These are the original matrices of
[exact wire contraction](research_mixed_wire_exact_contraction.md);
all triangular support zeros and normals remain.

For either external type, the new vertex is an ordinary bidisk
map. Its legs lie in
\[
 P_3=\{|z-c_3|<.083\},\qquad P_4=\{|z-c_4|<.060\}.
                                                               \tag{9}
\]
The proof of Proposition 1 of
[the critical-height theorem](research_mixed_cyclic_critical_height_bounds.md)
establishes these image bounds on the entire typed input products
before cyclic specialization. The preceding leg in (6) is the
actual last leg of the old word, including an attached endpoint
when the old length is one. It is in its typed disk, so that same
bidisk scope applies.

Keep all old and new variables before elimination. Their roots
have distance \(>1/1000\) from the boundaries of the larger
\(U,E,Q\) product, by the
[endpoint ranges](research_mixed_open_word_endpoint_rectangles.md),
the typed disks, and (9). Their first private coordinates remain
in the established endpoint-symbol rectangle as well.
Let \(B_3\ge1\) bound \(|J'''|\) on the finitely many primitive
argument strips. The sparse-row calculation in the previous theorem
gives, independently of the word length,
\[
          \|F''(z)-F''(\widetilde z)\|_2
                         \le10B_3\|z-\widetilde z\|_2.          \tag{10}
\]
Only the pure-imaginary quadratic chirps have been omitted from
this derivative difference; they are still present in \(F\).
No value of \(B_3\) is evaluated here.

Put
\[
 d=1/500,\qquad
 \rho_*=\min(1/1000,\mu/(80B_3)),\qquad
 \varepsilon_*=\min(\mu\rho_*/8,\mu d/8).                       \tag{11}
\]
Consider a holomorphic perturbation \(P_h\) with \(P_h'=h\).
It suffices that \(|h|\le\varepsilon_*\) on each of the disks
\[
              |b-c_3|\le.086,\qquad |b-c_4|\le.063.             \tag{12}
\]
At an actual new input \(r\), a displacement of at most
\(\rho_*\) and a Cauchy circle of radius \(d=.002\)
stay in the corresponding disk (12). Thus
\(|h'|\le\varepsilon_*/d\).
The frozen-original-inverse fixed-point map in the
\(\rho_*\)-ball has derivative at most
\[
          (10B_3\rho_*+\varepsilon_*/d)/\mu\le1/4
                                                               \tag{13}
\]
and center displacement at most \(\varepsilon_*/\mu\le\rho_*/8\).
It is a strict self-map, uniformly in the word, both letters,
and both external disks. Its unique root has displacement at most
\(2\varepsilon_*/\mu\le\rho_*/4\). In particular
\[
 r_{\alpha,h}(D_\beta)\subset
 \begin{cases}
  \{|r-c_3|<.084\},&\alpha=0,\\
  \{|r-c_4|<.061\},&\alpha=1,
 \end{cases}\qquad \beta=3,4.                                \tag{14}
\]
Here and below \(D_\beta\) in a mapping assertion may be read
via holomorphic continuation from its interior.

On the overlap of the external disks the two perturbed roots agree:
their original centers agree, the equations use the same \(h\),
and the same contraction ball has a unique zero. Therefore the
perturbed output is one holomorphic phase on \(\Omega\), with
the same constant in both charts. Its full negative real Hessian
and every accretive Schur elimination retain the floor \(7\mu/8\),
because the sole additional Hessian entry has modulus
\(\le\varepsilon_*/d\le\mu/8\).

## 3. The two-radius gradient norm and its contraction

For a holomorphic function on \(\Omega\), define
\[
 \|h\|_*=\max_{\beta=3,4}
 \sup_{b\in\operatorname{int}D_\beta}
       R_\beta\left(1-\frac{|b-c_\beta|^2}{R_\beta^2}\right)|h(b)|.
                                                               \tag{15}
\]
The factors \(R_\beta\) are essential when the input and output
typed radii differ. This is a norm on the compatible functions,
not two independent disk norms. Its finite-norm space is complete:
a Cauchy sequence converges uniformly on compact subsets of each
disk, the limits agree on their overlap, and the weighted suprema
give convergence in (15).

Set
\[
 m_*=\min\left[
 R_3\left(1-\frac{.086^2}{R_3^2}\right),
 R_4\left(1-\frac{.063^2}{R_4^2}\right)\right]
 =\min(44/5625,127/64000)=127/64000,\qquad
 \delta_*=m_*\varepsilon_* .                                  \tag{16}
\]
Every \(\|h\|_*\le\delta_*\) satisfies (12), even if it is
unbounded near the boundary of \(\Omega\). Define its primitive
by
\[
                    P_h(b)=\int_{b^\dagger}^b h(z)\,dz.
                                                               \tag{17}
\]
Simple connectedness makes it path-independent.

Let \(h^+_{w,\alpha}\) be the derivative of
\(\mathscr T_\alpha[H_w+P_h]-H_{w(3+\alpha)}\).

**Theorem 1.** Both letters map the common closed and open
\(\delta_*\)-balls into themselves, and
\[
 \|h^+_{w,\alpha,1}-h^+_{w,\alpha,2}\|_*
       \le\lambda_\alpha\|h_1-h_2\|_*,
 \qquad
 \lambda_0=14/15,\quad \lambda_1=61/64,\quad
 h^+_{w,\alpha,0}=0 .                                        \tag{18}
\]
These constants do not depend on the old word or the external type.

*Proof.* Interpolate \(h_\theta=(1-\theta)h_2+\theta h_1\).
Symmetry of the original stationary Hessian gives exactly
\[
 \partial_\theta h^+_{w,\alpha,\theta}(b)
         =r_{\alpha,\theta}'(b)
                   (h_1-h_2)(r_{\alpha,\theta}(b)).             \tag{19}
\]
This is differentiation at the actual perturbed root, with no
approximate tangency. For \(b\in\operatorname{int}D_\beta\),
normalize
\[
 z=(b-c_\beta)/R_\beta,\qquad
 f(z)=(r_{\alpha,\theta}(b)-c_{3+\alpha})/R_{3+\alpha}.
\]
By (14), \(|f|<\lambda_\alpha\). Schwarz--Pick for
\(f/\lambda_\alpha\) implies
\[
 \frac{R_\beta(1-|z|^2)|r_{\alpha,\theta}'(b)|}
 {R_{3+\alpha}(1-|f(z)|^2)}
 \le\lambda_\alpha
       \frac{1-|f(z)|^2/\lambda_\alpha^2}{1-|f(z)|^2}
 \le\lambda_\alpha .                                        \tag{20}
\]
Multiplying (19) by the output weight, and using the input
weight at its image point, proves (18) after integration in
\(\theta\). Both charts give the same analytic output by
Section 2. The zero error gives (7), proving invariance.
\(\square\)

Hence along any prescribed positive letter sequence,
\[
                         \|h_j\|_*\le(61/64)^j\|h_0\|_* .
                                                               \tag{21}
\]
The moving centers are the actual phases \(H_{w_j}\), not a
single fixed alternating germ. This establishes a common open
local phase class for arbitrary concatenation.

## 4. Every original action increment is retained

Write an admitted phase as
\[
       A+H_w(b)-H_w(b^\dagger)+P_h(b).                         \tag{22}
\]
Its new constant is \(A+C_{w,\alpha}(h)\), with
\[
\begin{split}
 C_{w,\alpha}(h)
   &=\mathscr T_\alpha[H_w-H_w(b^\dagger)+P_h](b^\dagger),\\
 C_{w,\alpha}(0)
   &=H_{w(3+\alpha)}(b^\dagger)-H_w(b^\dagger).
\end{split}                                                     \tag{23}
\]
After subtracting that value, its normalized output is exactly
\(H_{w(3+\alpha)}-H_{w(3+\alpha)}(b^\dagger)+P_{h^+}\).
Thus no constant is reset to a bulk value.

For a stationary input in the type-\((3+\alpha)\) disk,
integrate (17) along
\(b^\dagger\to c_{3+\alpha}\to r_{\alpha,h}\). The norm gives
\[
 |P_h(r_{\alpha,h})|
 \le\left[
 \operatorname{atanh}\frac{|b^\dagger-c_{3+\alpha}|}{R_{3+\alpha}}
       +\operatorname{atanh}\lambda_\alpha\right]\|h\|_*
 <3\|h\|_* .                                                 \tag{24}
\]
Here (3) gives
\(|b^\dagger-c_\nu|/R_\nu<3/5\).
The bracket is at most
\(\frac12\log4+\frac12\log(125/3)=\frac12\log(500/3)<3\);
the last elementary inequality follows from
\(e^6>\sum_{j=0}^5 6^j/j!=899/5>500/3\).
No decimal or logarithm evaluation is used.

Stationarity cancels the derivative of the moving root, so
\(\partial_\theta C_{w,\alpha}(\theta h)=P_h(r_{\alpha,\theta h})\).
Consequently
\[
 |C_{w,\alpha}(h)-C_{w,\alpha}(0)|\le3\|h\|_*,
 \qquad
 \sum_{j\ge0}
 |C_{w_j,\alpha_j}(h_j)-C_{w_j,\alpha_j}(0)|
                  \le64\|h_0\|_* .                            \tag{25}
\]
This controls perturbations of the actual action sequence. It
does not identify the actions of different words or give a
simultaneous asymptotic in word length and quantum level.

## 5. The compatible local leading amplitudes

There is also an operation-preserving class at the leading-symbol
level. This does not require a whole-source estimate.
Let
\[
 \mathfrak a(z)=\sqrt{2\sin\pi z}\,e^{-i\pi z/2}
\]
with its original factorial branch. The new literal
\(B_{3+\alpha}\Gamma\) row in (8) has scalar
\(\kappa_N^{1+\alpha}N^{-1}\), phase
\(V_\alpha(r,t)+G(t,b)\), and symbol
\[
 k_\alpha(r,t;b)
   =\frac{\mathfrak a(r+t)\mathfrak a(t+b)}
          {\mathfrak a(r)^\alpha
           \mathfrak a(t)^{\alpha+2}\mathfrak a(b)^2}.           \tag{26}
\]
The original \(B_4\) factor \(N\) has been included here.
Both letters therefore have the same row power \(N^{-1}\).
Every argument in (26), on the domains in Section 2, stays
in one fixed compact subset of \(0<\Re z<1\).
Thus \(k_\alpha\) and its reciprocal are uniformly bounded.

For the stationary phase in (6) with perturbation \(P_h\),
let \(S_{w,\alpha,h}\) be its reduced two-variable negative
Hessian at the root. It has accretivity floor \(7\mu/8\).
The original oriented Gaussian factor is
\[
 m_{w,\alpha,h}(b)=
   \frac{2\pi\, k_\alpha(r_{\alpha,h}(b),t_{\alpha,h}(b);b)}
                   {\sqrt{\det S_{w,\alpha,h}(b)}} .            \tag{27}
\]
It is holomorphic and nonzero on \(\Omega\).
The square root is the accretive Gaussian continuation.
Equivalently its logarithm comes from the matrix logarithm on
the accretive matrix domain, so no independent square-root
choices are made on the two disks.

There is a single finite constant \(M_0\), independent of the
word, letter and admitted perturbation, such that
\[
                   \|(\log m_{w,\alpha,h})'\|_*\le M_0.
                                                               \tag{28}
\]
Here is a direct justification of uniformity. Formula (5) bounds
\(H_w''\), while \(H_w'''\) at the strict inner input images
is bounded by Cauchy estimates applied to the uniformly bounded
\(H_w'\). The same inner Cauchy disks bound \(h'\) and \(h''\).
Thus the reduced Hessian and its derivative along \(b\) are
uniformly bounded: the root derivatives follow by multiplying
the fixed-size boundary coupling by \(S^{-1}\), whose norm is
at most \(8/(7\mu)\).
The primitive symbol and its logarithmic derivatives are uniformly
bounded on the compact regular domains. Differentiating
\(\log\det S\) gives \(\operatorname{tr}(S^{-1}S')\).
These formulas bound the ordinary derivative of \(\log m\)
uniformly on each disk, hence give (28).
This argument does not differentiate the growing determinant
of an entire long word or assume its bound.

Take a normalized local amplitude \(f=e^\ell\), with
\(\ell(b^\dagger)=0\) and \(\|\ell'\|_*\le M\).
Its exact new leading scalar and normalized logarithm are
\[
\begin{split}
 \mu_{w,\alpha}(h,\ell)
     &=m_{w,\alpha,h}(b^\dagger)
                      e^{\ell(r_{\alpha,h}(b^\dagger))}\ne0,\\
 \ell^+(b)
     &=\log\frac{m_{w,\alpha,h}(b)}
                     {m_{w,\alpha,h}(b^\dagger)}
       +\ell(r_{\alpha,h}(b))
       -\ell(r_{\alpha,h}(b^\dagger)).
\end{split}                                                     \tag{29}
\]
The logarithm vanishing at \(b^\dagger\) exists on the simply
connected union. Equation (20) now yields
\[
                    \|(\ell^+)'\|_*
                          \le M_0+(61/64)M .                   \tag{30}
\]
Every \(M\ge64M_0/3\) is invariant. For a fixed phase, the
difference of two amplitude logarithmic derivatives contracts
by at most \(61/64\). No contraction of an unweighted joint
phase/amplitude norm is asserted.

There are uniform \(0<m_-\le m_+<\infty\) with
\(m_-\le|m_{w,\alpha,h}|\le m_+\). The numerator in (27)
is bounded above and away from zero on its fixed compact domain;
the singular values of \(S\) have a positive lower bound and a
finite uniform upper bound. Applying the path estimate (24) to
\(\ell'\), one therefore obtains
\[
 m_-e^{-3M}\le|\mu_{w,\alpha}(h,\ell)|\le m_+e^{3M}.             \tag{31}
\]
Thus every local coefficient multiplier is quantitatively nonzero.

The two actual one-letter cut currents have nonzero holomorphic
coefficients on neighborhoods of both closed disks, by the original
endpoint maps and full endpoint-coefficient packet. More explicitly,
for each own type and either external disk the three-variable
endpoint map puts the private index in the full packet rectangle
\(E_{\rm cap}\). The original coefficient \(b_N(s)=D_N(s)^{-1}C_N(s)\)
has its nonzero packet there, as used in
[the literal prefix theorem](research_mixed_fourier_prefix_local_current.md).
The one vertex and the final \(\Gamma\) have their nonzero
factorial symbols. Eliminating the endpoint auxiliary and then the
two remaining local indices uses accretive Schur blocks, so its
Gaussian coefficient is nonzero and glues on the overlap. This is
the one-ordinary-cap map with a retained external leg, not the
different one-vertex problem with two ordinary caps. Compactness
gives a neighborhood of the entire pair of closed disks.
Their normalized logarithmic derivatives consequently have finite
norms. Choose \(M\) also
larger than those two norms. Then the actual leading coefficients
for all positive words belong to this local amplitude class:
the exact source (8) and Gaussian Schur associativity identify
the iterated local coefficients with the direct ones.

The local powers are unchanged. The incoming cut current has
power \(N^{-3/2}\), as proved in the previous note. The added
row contributes \(N^{-1}\), two new indices contribute \(N^2\),
and their Gaussian contributes \(N^{-1}\). Thus the outgoing
cut current again has \(N^{-3/2}\), with the retained multiplier
\(\kappa_N^{1+\alpha}\mu_{w,\alpha}(h,\ell)\).
These are local symbol assertions with the original orientations
at both parities. They do not make finite-\(N\) relative errors
uniform in word length.

## 6. Scope of the enlarged class

Every nonempty actual prefix belongs at phase error zero.
The common phase and amplitude neighborhoods allow arbitrary
subsequent positive letters, while retaining the actual ordinary
cap and every action/amplitude scalar. Four-ending members have
the original nondegenerate Fourier polarization from the preceding
phase theorem; no analogous unproved Fourier-output assertion
for three-ending members is needed here.

The disk union is a critical-phase domain, not the smaller
\(K_3,K_4\) source-envelope domain. In particular this result
does not use, and cannot repair, the
[disproved independent Fourier-endpoint inclusion](research_mixed_fourier_boundary_saved_domain_result.md).
Nor does the phase-gradient norm control the exact finite vectors
\(d_{w,N}\), their exterior currents, or the effect of changing
finite Fourier basis. A source induction must still prove its
whole-source estimates in this retained chart, or justify every
seam in a different chart. The completed local kernel near
\((x_0,x_0)\) is not extended by this theorem. Actual closed-knot
noncancellation and the cofinite-assignment target remain separate.

