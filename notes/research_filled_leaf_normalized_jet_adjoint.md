# The actual leaf jet Fourier observation away from its characteristic frequencies

Private written proof, 16 November 2026.

The normalized joint value-and-normal Fourier observation of an
original filled leaf has an exponentially accurate reduction to
two explicit endpoint packets. This holds away from its actual
characteristic frequencies, for every fixed integer power and
every fixed number of microscopic endpoint factors. It uses the
entire source companion, including gauged and recovery channels.
No holomorphic bound for the source between physical rows is used.

The analytic-probe construction is already in the whole-kernel Ward
note. The new input here is its application to the actual full-normal
leaf companion, the simultaneous normalized prefix budget for that
companion, and the identification of its signed frequency sectors.
The endpoint packets remain part of the observation.

## 1. Source, jets, and the full normalized state

Fix an integer \(n\), an integer \(r\ge0\), and bounded complex
microscopic parameters \(|\alpha_i|\le A\). Use
\[
 F_N=T(R^nB_N),\qquad
 B_N=\operatorname{can}\prod_{i=1}^rK_N(2\cosh(\alpha_i/N),Z),
 \qquad c_N(u)=2\cos(2\pi u+\pi/N).
 \tag{1}
\]
Here the algebra is the original full quotient by
\(P_N(Z)=2T_N(Z/2)+2\); \(T\) is the original turn, whereas
\(T_N\) is Chebyshev's polynomial. All carriers and product-rule
normals in (1) are retained. If \(r=0\), pad by the exact constant
\(K_N(c_0,Z)=1\), using the fixed parameter \(\alpha=i\pi\).
Thus the companion construction below may always use \(r\ge1\).

Fix \(I=[a,b]\Subset I_0\Subset(0,1/2)\), with \(a<b\), and put
\(h=N^{-1}\), \(u_j=jh\). For \(|n|=m\ge2\), retain the phase and
its additive constant from the action-calibration theorem:
\[
 S_{-m}(t)=\overline{S_m(\bar t)},\qquad
 S_m(\pi)=-i\pi/m,\qquad
 {\cal S}_h(u)=S_n(\pi-2\pi u-\pi h).
 \tag{2}
\]
For \(n=0,\pm1\), put \({\cal S}_h=0\). This last convention
records their subexponential bound, not a stationary phase.
All these functions are holomorphic on a fixed neighborhood of
\(I_0\) for sufficiently small \(h\). Denote the \(h=0\) function
by \({\cal S}_0\).

Let
\[
 v_j=F_N(c_N(u_j)),\qquad
 d_j=\left.\partial_u F_N(c_N(u))\right|_{u=u_j},
\]
\[
 a_j=e^{-{\cal S}_h(u_j)/h}v_j,\qquad
 b_j=e^{-{\cal S}_h(u_j)/h}
               [d_j-h^{-1}{\cal S}_h'(u_j)v_j].
 \tag{3}
\]
Every node in the buffered window is double. Thus \(d_j\)
retains its actual first spectral normal, multiplied by the
nonzero factor \(c_N'(u_j)\).

We specify the finite state used below. For \(n\ne0\), use exactly
the actual companion (18) of the literal leaf source, with its
gauged channels \({\cal F}\), recovered product \(F\), and their
first \(u\)-normals. For \(n=0\), use (19) of the first-turn
initialization source. Their state dimensions are fixed once
\(n,r\) are fixed. Divide both normal blocks by \(N\), and write
the resulting state and matrix as
\[
 Y_j=(X_j^{\cal F},hZ_j^{\cal F},X_j^F,hZ_j^F)^{\mathsf T},
 \qquad Y_{j+1}={\mathsf M}_h(u_j)Y_j .
 \tag{4}
\]
The component selectors \(e_v,e_d\), written as rows, select
the central value \(F_N(c_N(u_j))\) and its \(h\)-scaled
normal, respectively. Hence \(e_vY_j=v_j\), \(e_dY_j=hd_j\).
All shifted entries in the windows are still present.

Normalize the *whole* state by its base-row phase:
\[
 X_j=e^{-{\cal S}_h(u_j)/h}Y_j,\qquad
 X_{j+1}={\mathsf Q}_h(u_j)X_j,
\]
\[
 {\mathsf Q}_h(u)=
 \exp\!\left(\frac{{\cal S}_h(u)-{\cal S}_h(u+h)}h\right)
                  {\mathsf M}_h(u).
 \tag{5}
\]
The same base factor is used for every shifted entry. Define
\[
 \ell_h(u,\xi)=e_d-[{\cal S}_h'(u)+2\pi i\xi]e_v .
 \tag{6}
\]
Then the exact normalized Fourier observation is
\[
 {\mathfrak c}_N(\xi)
   =\sum_{j=j_0}^{j_1}(b_j-2\pi iN\xi a_j)e^{-2\pi i\xi j},
 \qquad
 h{\mathfrak c}_N(\xi)
   =\sum_{j=j_0}^{j_1}e^{-2\pi i\xi j}\ell_h(u_j,\xi)X_j .
 \tag{7}
\]
The indices may form any nonempty interval with \(u_j\in I\).
The packet at \(j_1+1\), needed below, lies in the buffer.

**Lemma 1 (actual matrix and prefix bounds).** On a sufficiently
small fixed complex neighborhood of \(I_0\), the matrices in (4)
and (5) are holomorphic and uniformly bounded, together with
every fixed derivative, for bounded complex \(\boldsymbol\alpha\).
They have bounded analytic expansions at \(h=0\), and
\[
 {\mathsf Q}_0(u)=e^{-{\cal S}_0'(u)}{\mathsf M}_0(u).
 \tag{8}
\]
For the actual states on the buffered real grid,
\[
 {\cal B}_N:=
 1+\sup_{\boldsymbol\alpha}
        \max_{j:\,u_j\in I_0}\|X_j\|,
 \qquad \log{\cal B}_N=o(N).
 \tag{9}
\]
The maximum can include any fixed number of adjacent rows.

*Proof.* In the literal leaf system, the two normalized scalar
extremes are nonzero on any compact interior chart. They are
the explicit finite products of the original sine coefficients,
the factor \(d_k\to1\), and the nonzero crossing phases.
The recovery extreme is likewise a finite nonzero sine product.
All denominators stay away from zero on a smaller complex
neighborhood for small \(h\). The cleared finite-degree
coefficients \(d,E\) have bounded analytic expansions in \(h\)
on the fixed parameter polydisk. This proves the matrix
assertion for \(n\ne0\).

For \(n=0\), the actual highest coefficient includes the matrix
\[
 d_k(c_N(u+kh)-c_0)I-s^2E_k,\qquad s=2i\sin(\pi h).
 \tag{10}
\]
Its limit is \((2\cos(2\pi u)-2)I\), a unit on the buffered
bulk chart. Thus its actual inverse is bounded and holomorphic
there for small \(h\). This retains the highest-order correction;
it is not a principal-symbol division at an endpoint.

After scaling the normals, the precise block form is
\[
 {\mathsf M}_h=
 \begin{pmatrix}
 A_{\cal F}&0&0&0\\
 hA_{\cal F}'&A_{\cal F}&0&0\\
 B&0&A_F&0\\
 hB'&B&hA_F'&A_F
 \end{pmatrix}.
 \tag{11}
\]
Here \(B\) is the actual forced-recovery selector, and all primes
differentiate its ordinary coefficient functions. This proves
the assertion also for the normal and recovery blocks.
The exponent in (5) extends holomorphically to \(h=0\), since
it equals \(-\int_0^1{\cal S}_h'(u+th)\,dt\).

For completeness, the physical prefix argument applies to every
component of this state, not only to the recovered \(F\).
All gauged and recovery channels and their initial normals have
polynomial fixed-row source bounds in the literal leaf theorem.
Starting with those data, its left-end estimate and compact
prefix estimate give, simultaneously for the entire state,
\[
 h\log(1+\|Y_j\|)
 \le C\epsilon\log(e/\epsilon)
       +\int_\epsilon^{u_j}L_n(v)\,dv+o_\epsilon(1)
 \tag{12}
\]
on \(I_0\), for every sufficiently small fixed \(\epsilon>0\).
Fixed shifts in the windows change the compact integral only
by \(O(h)\). The multiple-root error divided by \(N\) tends
to zero for fixed \(\epsilon\). Taking the upper limit and
then \(\epsilon\downarrow0\) gives the upper exponent
\({\cal J}_n(u_j)=\int_0^{u_j}L_n\) for every channel.
For \(n=0\), the first-turn theorem supplies the simultaneous
subexponential bound directly; for \(n=\pm1\), (12) has
\(L_n=0\).

For \(|n|\ge2\), action calibration says
\(\Re{\cal S}_h(u)={\cal J}_n(u+h/2)\).
On this compact interval the half-row change costs a bounded
factor. Subtracting this phase in (12) proves (9).
All estimates are uniform on larger parameter polydisks.
No derivative of a value-only estimate was used. \(\square\)

## 2. The signed frequency sectors

The full matrix spectrum, with all multiplicities, is needed.
For \(n\ne0\), the principal gauged and recovery symbols are
\[
 (y-2)^{33r}(x_{-n}-2)I,\qquad (y-2)^r,
 \quad
 x=2\cos(2\pi u),\quad
 y-2=-\tan^2(\pi u)\tau^{-1}(\tau-1)^2 .
 \tag{13}
\]
Consequently the eigenvalues of \({\mathsf M}_0\) are the
unit source/recovery root and the selected terminal roots
of \(D_{-n}=2\), with their actual repeated multiplicities.
The normal blocks repeat this spectrum; recovery coupling does
not add eigenvalues. For \(n=0\), every eigenvalue is one,
by the exact first-turn principal system. No semisimplicity
is asserted.

**Lemma 2 (the actual phase argument).** If \(|n|\ge2\), then
\[
 e^{{\cal S}_0'(u)}=\tau_{\max,-n}(u),
 \tag{14}
\]
the unique selected forward root of \(D_{-n}=2\) with largest
modulus. Thus the only unit-modulus eigenvalue of
\({\mathsf Q}_0(u)\) is one, with its multiplicity retained.

*Proof.* First let \(n=m\ge2\). To avoid confusing the small
step \(h\) with an angle, put
\[
 H=\sin(\pi u),\quad a=\frac{H^2}{1-H^2},\quad
 \zeta U_{m-1}(\zeta)=iH,\quad
 \theta=\arccos\zeta .
 \tag{15}
\]
These are the dominant first-quadrant branch and its original
inverse-cosine lift from the action theorem. That theorem gives
\[
 {\cal S}_0'(u)=2\operatorname{asinh}(\zeta/\sqrt a).
 \tag{16}
\]
Set \(\tau=e^{{\cal S}_0'}\) and \(y=2-4\zeta^2\).
The original physical conic, with forward row shift fixed, is
\[
 y=2+2a-a(\tau+\tau^{-1}),\quad
 z=2+2a+a(e^{-2\pi iu}\tau+e^{2\pi iu}\tau^{-1}).
 \tag{17}
\]
Write
\[
 {\cal R}=\sqrt{H^2+(1-H^2)\zeta^2}.
 \tag{18}
\]
The square root is in the first quadrant: its squared
argument has positive imaginary part. Direct substitution
of (16) in (17) gives
\[
 z=2+4H^2+4(1-2H^2)\zeta^2-8iH\zeta{\cal R}.
 \tag{19}
\]

The signed terminal selection must still be checked.
The identities \(\sin(m\theta)=iH\tan\theta\) and
\(U_m(\zeta)=iH+\cos(m\theta)\) imply
\[
 [\zeta\cos(m\theta)]^2={\cal R}^2,\qquad
                   \zeta\cos(m\theta)=-{\cal R}.
 \tag{20}
\]
For \(m\ge3\), the minus sign follows as \(H\downarrow0\)
from \(\zeta\to\cos(\pi/m)>0\) and \(m\theta\to\pi\).
For \(m=2\), \(\zeta=e^{i\pi/4}\sqrt{H/2}\) and
\(\cos(2\theta)=iH-1\) give the same sign. Neither side
vanishes for \(0<H<1\), so continuity preserves it.
Using the exact polynomial identity
\(f_j(2-4\zeta^2)=2+4\zeta^2U_{j-1}(\zeta)^2\),
equations (19)--(20) yield
\[
                          z=f_{m+1}(y).
 \tag{21}
\]
Together with \(x=f_m(y)\), this is precisely the signed
selection for \(D_{-m}=2\), rather than \(D_m=2\).
The modulus is the unique largest modulus by the ordering
theorem. For negative \(n\), coefficient conjugation in the
physical shift convention and the definition of \(S_{-m}\)
prove (14). Finally all other terminal moduli are strictly
smaller, and the source root has modulus one before division
by \(e^{{\cal S}_0'}\), whose modulus exceeds one. \(\square\)

For clarity, the real frequency sectors modulo integers are
\[
 \Sigma_n(u)=
 \begin{cases}
 \{0\},& n=0\ \text{or }|n|\ge2,\\
 \{0,\ \tfrac12-nu\}\pmod{\mathbb Z},&n=\pm1 .
 \end{cases}
 \tag{22}
\]
Indeed \(D_{-1}=2\) has root \(-e^{-2\pi iu}\), and
\(D_1=2\) has root \(-e^{2\pi iu}\); the unit source root
remains. Since \({\cal S}_h=0\) for these powers, both are
unit-modulus roots of the normalized matrix. Equation (22)
is an exact classification of the *principal* Fourier
sectors, not a support assertion for the finite observation.

## 3. A bounded analytic adjoint for the complete companion

Let \(\Xi\subset\mathbb R\) be compact. Suppose
\[
 \operatorname{dist}_{\mathbb R/\mathbb Z}
       (\xi,\Sigma_n(u))\ge d>0
       \qquad (u\in I_0,\ \xi\in\Xi).
 \tag{23}
\]
One may first enlarge \(I\) slightly and then choose \(I_0\);
this supplies a positive buffer for the condition.
For \(|n|\ge2\), or \(n=0\), (23) simply excludes the
integer aliases by a fixed distance.

**Theorem 3.** There are constants \(C,\kappa>0\) and, for
all sufficiently large \(N\), holomorphic row vectors
\(v_N(u,\xi,\boldsymbol\alpha)\) and
\(r_N(u,\xi,\boldsymbol\alpha)\), on a fixed smaller
complex neighborhood of \(I\), such that
\[
 v_N(u,\xi)-e^{-2\pi i\xi}
                v_N(u+h,\xi){\mathsf Q}_h(u)
       =\ell_h(u,\xi)-r_N(u,\xi),
 \tag{24}
\]
\[
                 \|v_N\|\le C,\qquad
                 \|r_N\|\le C e^{-\kappa N}.
 \tag{25}
\]
The equation and bounds are uniform on \(\Xi\) and the
fixed complex parameter set. The right endpoint and its
one-step shift lie in the stated neighborhood. All fixed
parameter derivatives obey these bounds on smaller sets.

*Proof.* By (8), (13), and (22), the finite matrix
\[
 K_h(u,\xi)=I-e^{-2\pi i\xi}{\mathsf Q}_h(u)
 \tag{26}
\]
has a uniformly bounded holomorphic inverse \(B_h=K_h^{-1}\)
on a sufficiently small fixed complex neighborhood of
\(I_0\times\Xi\), for small \(h\). This follows from compactness
and the nonzero principal determinant, not from diagonalizing
or dropping any repeated root. Lemma 1 supplies uniform
holomorphic coefficient bounds there.

Put \(w=e^{-2\pi i\xi}\), and define an operator on analytic rows:
\[
 ({\cal T}_h f)(u)
    =w[f(u+h)-f(u)]{\mathsf Q}_h(u)B_h(u),\qquad
 f_h(u)=\ell_h(u,\xi)B_h(u).
 \tag{27}
\]
No multiplier is commuted past the shift.
For nested complex tubes of widths \(s,s+\delta\) around
the fixed interval, Cauchy's estimate gives
\[
 \|{\cal T}_h f\|_s\le \frac{C_0h}{\delta}\|f\|_{s+\delta},
                         \qquad \delta\ge2h.
 \tag{28}
\]
All norms are also uniform on slightly smaller fixed complex
frequency and exterior-parameter neighborhoods.

Choose a fixed total tube loss \(\Delta>0\), and
\[
 M\ge\max(1,2,C_0),\qquad
 k_N=\left\lfloor\frac{\Delta N}{4M}\right\rfloor,\qquad
 \delta_N=\Delta/k_N .
 \tag{29}
\]
For large \(N\), \(k_N\ge1\), the shift reserve holds, and
each application in (28) costs at most \(1/4\).
Define the finite analytic rows
\[
 v_N=\sum_{\ell=0}^{k_N-1}{\cal T}_h^\ell f_h,\qquad
 r_N=({\cal T}_h^{k_N}f_h)K_h .
 \tag{30}
\]
The last summand of \(v_N\) still has a tube layer before
its final shift. Finite telescoping yields
\((I-{\cal T}_h)v_N=f_h-{\cal T}_h^{k_N}f_h\).
Multiplying on the right by \(K_h\) proves exactly (24).
The geometric bounds give
\(\|v_N\|\le4\|f_h\|/3\) and
\(\|r_N\|\le C4^{-k_N}\). After reducing the fixed positive
exponent, these are (25). This is the analytic-probe method
of the pinned Ward source, now with the actual matrix
companion and its exact finite-\(h\) inverse. \(\square\)

## 4. Exact endpoint reduction of the Fourier observation

Use the *same* row \(v_N\) from Theorem 3 on the whole
buffered interval. For \(w=e^{-2\pi i\xi}\), define
\[
 {\cal P}_{j_0,j_1,N}(\xi)
 =w^{j_0}v_N(u_{j_0},\xi)X_{j_0}
   -w^{j_1+1}v_N(u_{j_1+1},\xi)X_{j_1+1}.
 \tag{31}
\]
These are actual complete companion packets, including
the gauged channels, shifted values, recovered product,
and their original first normals.

**Corollary 4.** Uniformly over all the intervals in (7),
all \(\xi\in\Xi\), and the fixed microscopic parameter set,
\[
 \boxed{\quad
 N^{-1}{\mathfrak c}_N(\xi)
     ={\cal P}_{j_0,j_1,N}(\xi)+{\cal E}_{j_0,j_1,N}(\xi),
 \quad
 {\cal E}_{j_0,j_1,N}
     =\sum_{j=j_0}^{j_1}w^j r_N(u_j,\xi)X_j ,
 \quad}
 \tag{32}
\]
\[
 |{\cal E}_{j_0,j_1,N}|
      \le CN e^{-\kappa N}{\cal B}_N
                       =e^{-\kappa N+o(N)} .
 \tag{33}
\]
The identity, including the displayed remainder, is exact.
The endpoint packet has only the presently proved bound
\[
                        |{\cal P}_{j_0,j_1,N}|
                                    \le C{\cal B}_N .
 \tag{34}
\]

*Proof.* Multiply (24), at \(u_j\), by \(w^jX_j\).
Use the exact physical recurrence (5). The two adjoint
terms become
\[
 w^jv_N(u_j)X_j-w^{j+1}v_N(u_{j+1})X_{j+1}.
 \tag{35}
\]
Summing telescopes, and (7) proves (32).
For real \(\xi\), \(|w|=1\); (9) and (25) prove
(33)--(34). No off-grid value of \(F_N\) was used. \(\square\)

If the integer interval is subdivided into adjacent intervals,
the artificial endpoint packets cancel exactly, because the
same \(v_N\) is used on their shared neighborhood. Different
local probes have their literal mismatch packet instead.
The two external endpoints of the full window do not cancel
by this argument.

The normalized combination in (7) is not periodic in \(\xi\),
because of the term \(2\pi i\xi a_j\). Only its characteristic
sector test is periodic. Thus on the midpoint Fourier interval
\([-1,1]\), the aliases at \(-1,0,1\) are all retained.
No finite Fourier mode or original trace alias has been removed.

## 5. Shared products and the original closing

The construction also applies to a fixed product of actual leaf
messages \(F^{(1)},\ldots,F^{(q)}\) at one common physical color.
Their powers and endpoint counts are fixed, and microscopic
parameters may be shared. Form the tensor of their exact states
in (4), and normalize by the common phase
\({\cal S}_h=\sum_i{\cal S}_{i,h}\).
The step matrix is the tensor product of the individual matrices.
The product value and scaled first normal are selected by
\[
 e_v^{\rm joint}=\bigotimes_i e_{v,i},\qquad
 e_d^{\rm joint}
    =\sum_i e_{v,1}\otimes\cdots\otimes e_{d,i}
                         \otimes\cdots\otimes e_{v,q}.
 \tag{36}
\]
These retain exactly the normal product rule. Equivalently
the normalized jets are
\[
 a_j=\prod_i a_{i,j},\qquad
 b_j=\sum_i b_{i,j}\prod_{\ell\ne i}a_{\ell,j}.
 \tag{37}
\]
Their full normalized tensor state has budget \(e^{o(N)}\).

Every normalized individual characteristic root has modulus
at most one. Hence the unit-modulus tensor roots are exactly
the products of the unit-modulus individual roots. The
frequency sectors are therefore the finite sum sets
\[
                       \Sigma_{\rm joint}(u)
                                =\sum_i\Sigma_{n_i}(u)
                                       \pmod{\mathbb Z}.
 \tag{38}
\]
Apply Theorem 3 away from this set. Equations (31)--(34)
then hold for the joint jets (37), with the entire tensor
endpoint packet retained. In particular, if all powers
have absolute value at least two, the sole normalized
sector is zero modulo integers. Repeated roots and
their source/recovery extensions remain in the matrix;
this is not a multiplication of selected scalar modes.

For placement in the original midpoint current, the
pinned pairing theorem gives, with its actual weighted
spectator transform \(\widehat A_N\) and remaining
original closing \(\Lambda_N\),
\[
 Z_{\rm int}
   =-\frac{\eta N}{\pi}
      \int_{-1}^{1}
       \Lambda_N\!\left({\mathfrak c}_N(\xi)
                                  \widehat A_N(\xi)\right)d\xi .
 \tag{39}
\]
On any part of this frequency interval satisfying (23),
one may insert the exact decomposition (32). Both endpoint
packets, the same joint spectator, the remainder, and
the same closing remain. The exterior half-boundaries
of the weighted-window construction are still present.
The estimate (33) is uniform on the specified parameter
sets *before* an otherwise unestimated closing is applied.
No bound for that closing or its spectator follows by
linearity.

Thus the new conclusion is phase-sensitive control of
the interior observation: off its genuine frequency
sectors, it is an explicit endpoint observation to
exponential accuracy. Bounding the external packets
after their actual shared closing, and the contribution
near the sectors in (22) or (38), are still required for
a parent-action estimate. Neither a smaller canonical
free-color norm nor source noncancellation is asserted.

## 6. Direct sources and readback

The complete direct sources were read at these unchanged
pins, with their used implications checked:

* [Literal filled-leaf source and complete companion](research_filled_leaf_endpoint_product_upper_bound.md),
  SHA256 5a5f9be510823289b97c1c4df6104d95156b43a881fe148adf592ed5b5adc844:
  ordered full source, exact signed extremes, all normal/recovery
  blocks, polynomial fixed-row data and simultaneous prefix bounds.
* [First-turn initialization](research_first_turn_endpoint_product_initialization.md),
  SHA256 7d0871a7dcde94c1cc73f98495b9521a61478729ddd52c51570ffa95f1901105:
  actual \(n=0\) highest matrix, all gauged channels and unit
  principal roots, with simultaneous subexponential bounds.
* [Strict terminal modulus ordering](research_terminal_twist_global_modulus_order.md),
  SHA256 79f26184f1ea0a4d45bb9961397175fc1fa6bad332482edd681a85156a6eae3a:
  original physical conic, signed selection, double multiplicities,
  and the unique maximal branch on every bulk compact.
* [Terminal phase and action calibration](research_terminal_characteristic_action_calibration.md),
  SHA256 582c359817b69b0dd1094e49878d15917230e86f6e7831fe448ea4aacee8a1fd:
  specified phase, principal branches, signed reflection,
  partial real action and its original endpoint constant.
* [Whole-kernel analytic adjoint probes](research_whole_kernel_adjoint_ward_localization.md),
  SHA256 43f0058f8eed882abe1ec548484786656b025274488ad12de80cda0fea42e540:
  prior nested-domain analytic-probe method and retained boundary
  currents. The exact matrix application is proved above.
* [Midpoint full-normal Fourier pairing](research_leaf_interface_midpoint_fourier_pairing.md),
  SHA256 d24bf81b7ab841022ec72fb1e6af2d76e03aea057f749c0e60d350e200784083:
  the exact observation (7), original closing coefficient (39),
  direct shared products, and retained exterior half-boundaries.

The specialized seven-term local-adjoint and variable-frequency
notes were inspected for coverage. They do not supply the
all-power literal-leaf companion, signed centering, or joint
normal observation used here.

Only written mathematics and source-text/hash reads were used.
No mathematical program, numerical experiment, test, or build
was run. Adopted notes and public manuscripts are unchanged.
