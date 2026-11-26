# A coherent main sheet for every four-ending Fourier prefix

Research deduction, 7 November 2026. For every fixed positive
three/four prefix of length at least two ending in four, the whole
first cap controls the entire central sheet of the remaining literal
factorial source. Its original marginal cancels exactly, and a
chain of accretive pair forms supplies a quadratic loss throughout
the independent outer box. The argument uses the individual cap
profile bounds; it never divides by a finite Fourier weight.

The physical complement and contour corrections are separate.
The last section records which existing uniform results do and do
not provide them. No function or saved calculation is evaluated.

## 1. The literal contraction and its actual reference

Keep the notation and exact source (4) of
[the Fourier-prefix local-current theorem](research_mixed_fourier_prefix_local_current.md).
Thus the word has flags \(\epsilon_1,\ldots,\epsilon_m\), with
\[
 m\ge2,\qquad \epsilon_m=1,\qquad
 \alpha=\epsilon_1,\quad k=\sum_{j=1}^m\epsilon_j,
 \quad G_N(y,w)=v_N(w)^T A_{3+\epsilon_1}\cdots A_{3+\epsilon_m}h_N(y).
 \tag{1}
\]
All matrices, ordinary colors, chirps and scalars are original.
Write \(r=e^{-2\pi i/N}\), \(Q=r^{-1}\),
\(P_a=(r;r)_a\), \(Y=e^{2\pi iy}\), and
\(c_y=N^{-1}e^{-\pi i(N-1)y}(1-Y^N)\).
The exact first-index sum is
\[
 \sum_{i_1+j_1<N}b_{i_1}(w)
       \frac{P_{i_1+j_1}}{P_{i_1}^{\alpha}P_{j_1}^{\alpha}}
   =P_{j_1}^{\,1-\alpha}U_{\alpha,N}(w,r^{j_1}).
 \tag{2}
\]
Here \(U_{\alpha,N}\) is its whole degree-less-than-\(N\)
polynomial. Equation (2) is a physical-node identity; after it is
inserted into the entire finite sum, keep \(U_{\alpha,N}\) as
that polynomial at every complex outgoing argument.

In particular the exact contracted source is
\[
\begin{split}
 G_N={}&\kappa^{m+k}N^kc_y
 \sum_{\Omega'_N}
 U_{\alpha,N}(w,r^{j_1})P_{j_1}^{\,1-\alpha}
       \frac{Y^{j_m}}{(Y;r)_{j_m+1}}\\
 &\quad{}\times
 \prod_{j=2}^m\frac{P_{i_j+j_j}}{(P_{i_j}P_{j_j})^{\epsilon_j}}
 \prod_{j<m}
       \frac{Q^{j_ji_{j+1}}P_{j_j+i_{j+1}}}
                    {P_{j_j}^2P_{i_{j+1}}^2}.
\end{split}
 \tag{3}
\]
The remaining support \(\Omega'_N\) retains
\(0\le j_1<N\), \(i_j+j_j<N\) for \(j\ge2\), and
\(j_j+i_{j+1}<N\) for \(j<m\), with nonnegative indices.
No physical endpoint, selected component implicit in the original
matrix, normal term or Fourier sector has been discarded.

At \((y,w)=(x_0,-2)\), the
[critical-existence theorem](research_mixed_fourier_boundary_critical_existence.md)
gives the original reference. Put
\[
 z=(t_1,s_2,t_2,\ldots,s_m,t_m),\qquad
 z_*=x_*+ih,\qquad P=[.22,.45].
 \tag{4}
\]
The full typed images place \(x_*\) strictly inside \(P^{2m-1}\),
and \(|h_j|<.12\). In particular the attached first leg has
real part in \((.246,.391)\), and all remaining ordinary legs
are in the smaller disks of
[full-bidisk image coverage](research_mixed_cyclic_critical_height_bounds.md),
Proposition 1. The last leg has type four and negative height;
thus the original outgoing Pochhammer remains in its unit-disk
domain on the whole sheet \(P^{2m-1}+ih\).

### The first-cap source restrictions are satisfied

For a type-three incoming neighbor, the first-cap certificate
allows the full original \(D_3\). For a type-four neighbor, its
full ordinary image lies in
\[
 P_4=\{|b-(.30-.052i)|\le.060\},
                    \qquad -.108<\Im b<-.001 .
 \tag{5}
\]
Only the own-four/input-four family has further restrictions.
Set \(b=s_{2,*}\), \(a=t_{1,*}=E_4(b)\), and
\(t=t_{2,*}\). The oriented full-bidisk image bound in
[the cap input-domain theorem](research_mixed_first_cap_oriented_plateau_certificate.md),
equations (1)--(5), gives \(\Re b>.259\): \(b\) is the
output adjacent to the own-four attached leg \(a\).

The original equations of vertex 2 also give precisely the inverse
identities of
[the coupled source domain](research_mixed_first_cap_coupled_plateau_certificate.md),
equations (1)--(2), with opposite leg \(t\in P_4\) and
next exterior leg
\[
 c=\begin{cases}
 s_{3,*},&m\ge3,\\
 \beta_K(t_{2,*}),&m=2.
 \end{cases}
 \tag{6}
\]
For \(m\ge3\), the full typed map places \(c\) in
\(P_3\cup P_4\), where
\(P_3=\{|c-(.35-.01i)|\le.083\}\).
For \(m=2\), the completed Fourier-boundary inclusion gives
\[
 |\beta_K(t_{2,*})-(.35-.01i)|<.082<.083.
 \tag{7}
\]
This shortest Fourier prefix still has an ordinary second vertex.
It therefore belongs to the **inverse-feasible** part of the
certificate's admissible union; it need not satisfy the different
fixed-point relation for an ordinary two-endpoint word.
The source comparison was proved on that entire admissible set,
not only on points realized by ordinary-ended words.
All lifts in (6) are the original ones.

Consequently the completed first-cap profile inequalities apply
to the present reference for every first type and every \(m\ge2\).
The private and attached endpoint images have their original
strict margins. These conclusions persist on a sufficiently small
parameter neighborhood for each fixed prefix.

## 2. Recovering a bare cap bound without division

Let \(T_\alpha(t)=\mathcal T_\alpha(t,-2)\) be the
additively calibrated complete cap action, and put
\[
 L_\alpha(t)=T_\alpha(t)-\frac{\alpha}{2}g(t),\qquad
 d=t_R-\Re t_{1,*},\qquad \kappa_0=1/2500000,
\]
\[
 B_L(t_R)=\Re L_\alpha(t_{1,*})
               +\Re L_\alpha'(t_{1,*})d-\kappa_0d^2 .
 \tag{8}
\]
Use the actual attached height \(h_1=\Im t_{1,*}\) and
actual private main height. Sections 2--3 of
[the complete upper-target cap theorem](research_mixed_cap_upper_target_completion.md)
establish the individual inequalities
\[
 A_{\alpha,i}(t_R+ih_1)
               -\frac{\alpha}{2}\Re g(t_R+ih_1)
                   \le B_L(t_R),\qquad t_R\in P .
 \tag{9}
\]
The \(A_{\alpha,i}\) are all five original regular source
profiles: private main, two real cuts and two penalized aliases.
The separate true-index ceiling satisfies the same inequality,
with a strict reserve. The proof of that theorem establishes
(9) before the allocated finite Fourier bound is applied.

Insert (9) into the literal whole-cap envelope. For every
\(\eta>0\), this yields the **bare** estimate
\[
 |U_{\alpha,N}(w,e^{-2\pi i(t_R+ih_1)})|
 \le C_\eta N^{a_\eta}
 \exp N\left\{B_L(t_R)+
          \frac{\alpha}{2}\Re g(t_R+ih_1)+\eta\right\}.
 \tag{10}
\]
It retains all private physical tails, joining currents and aliases,
both parities and fixed ordinary-color jets, on the original small
color neighborhood. This is a phase-profile deduction. Neither
\(d_N\) nor a square root of it is divided out, and no nonvanishing
claim about \(d_N\) on the whole target interval is needed.

## 3. The exact residual chain and its uniform curvature

For \(V(a,b)=g(a+b)-g(a)-g(b)\), define
\[
\begin{split}
 R_m(z)={}&
 \sum_{j<m}V(t_j,s_{j+1})
       +\sum_{j=2}^mV(s_j,t_j)\\
 &-\alpha g(t_1)
       -\sum_{j=2}^m\epsilon_j g(s_j)
       -\sum_{j=2}^{m-1}\epsilon_j g(t_j)\\
 &+2\pi i\sum_{j<m}t_js_{j+1}+\ell_{t_m}(x_0),\\
 R_m^{\rm a}(z)={}&R_m(z)+\frac{\alpha}{2}g(t_1).
\end{split}
 \tag{11}
\]
Expansion of the exact phase (7) of the local-current theorem gives
\[
 F_{\boldsymbol\epsilon}(s_1,z)
       =\Psi_\alpha(s_1,t_1)+R_m(z),\qquad
 \Phi_{\boldsymbol\epsilon}
       =L_\alpha(t_{1,*})+R_m^{\rm a}(z_*).
 \tag{12}
\]
The last equality uses the original cap critical value and its
absolute additive constant. The last leg has no extra single-leg
term in (11), precisely because \(\epsilon_m=1\).

**Lemma.** There is \(\mu_P>0\), independent of the length and
type pattern, such that
\[
              -\Re(R_m^{\rm a})''\succeq\mu_P I_{2m-1}
                       \quad\hbox{on }P^{2m-1}+ih .
 \tag{13}
\]

*Proof.* The original symmetric pair inequality
[proved on the full height domain](research_mixed_terminal_symmetric_pair_costs.md)
gives, for both real parts in \(P\) and absolute heights at
most \(.12\),
\[
 -\Re V''(a,b)\succeq
           \tfrac12\operatorname{diag}(\Re g''(a),\Re g''(b)).
 \tag{14}
\]
All sums lie in the regular strip. On this fixed compact product
\(\Re g''\) has a strictly positive minimum, because
\[
 \Re g''(x+iv)=
 \frac{\pi\sin(2\pi x)}
             {\cosh(2\pi v)-\cos(2\pi x)}>0,
                 \qquad .22\le x\le.45.
 \tag{15}
\]
An explicit choice is
\[
                         \mu_P=\frac9{46}.
 \tag{15a}
\]
Indeed \(\sin(2\pi x)\ge\sin(\pi/10)
=(\sqrt5-1)/4>3/10\) on \(P\), while the already proved
\(\cosh(.24\pi)<13/10\) gives
\(\cosh(2\pi v)-\cos(2\pi x)<23/10\).
Thus \(\Re g''>3\pi/23>9/23\). The pairs in (11)
form the connected chain on the \(2m-1\) variables in (4);
every variable has at least one pair incidence. Summing (14)
therefore supplies (13) already.

All remaining single-leg terms in \(R_m^{\rm a}\) have
nonpositive coefficients: in particular the first is
\(-\alpha g(t_1)/2\), not \(+\alpha g(t_1)/2\).
They add nonnegative negative-real-Hessian forms by (15).
The chirps have zero real Hessian. Finally
\(-\Re\ell_{t_m,t_mt_m}(x_0)>0\), since
\(0<\Re(t_m-x_0)<1/2\) and the original denominator is
regular. This proves (13) without a length-dependent estimate.
\(\square\)

At the original reference, stationarity gives
\[
 \partial_{t_1}R_m^{\rm a}(z_*)=-L_\alpha'(t_{1,*}),
 \qquad \partial_jR_m^{\rm a}(z_*)=0\quad(j\ne t_1).
 \tag{16}
\]
Integrating (13) from the actual center, and using (8), cancels
these full original complex marginals. For every independent
\(x\in P^{2m-1}\),
\[
 B_L(x_1)+\Re R_m^{\rm a}(x+ih)
 \le M_{\boldsymbol\epsilon}
       -\frac{\mu_P}{2}\|x-x_*\|^2
       -\kappa_0(x_1-x_{*,1})^2 ,
 \quad M_{\boldsymbol\epsilon}=\Re\Phi_{\boldsymbol\epsilon}.
 \tag{17}
\]
Equation (10) and the remaining literal factorial factors of (3)
therefore control the **whole coherent main sheet**, not merely
its local saddle neighborhood.

**Uniform main-face corollary.** Every outer face at the actual
critical heights has upper rate below
\(M_{\boldsymbol\epsilon}-1/40000\), independently of the length
and type pattern.
Indeed the attached first real coordinate lies in
\((.246,.391)\); a remaining type-three leg has real part in
\((.267,.433)\), and a remaining type-four leg in \((.24,.36)\).
The latter intervals are exactly the smaller disk image bounds
used above, and the former is the complete endpoint image bound
in the first-cap theorem. Each coordinate is therefore at distance
greater than \(17/1000\) from the boundary of \(P\).
On any face (17) loses strictly more than
\[
             \frac9{92}\left(\frac{17}{1000}\right)^2
                        >\frac1{40000}.
 \tag{17a}
\]
The last inequality is \(2601>2300\) after multiplying by
\(92000000\). This is a rate margin on the critical-height sheet;
it is not a comparison for the same real face at height zero.

The exact symbol is regular throughout this sheet: all vertex and
wire sums have real parts in \([.44,.90]\), and the outgoing
last-four height gives \(|Y|,|Ye^{-2\pi it_m}|<1\).
Near \(z_*\), the complete \(U_\alpha\) packet and the original
factorial symbols are nonzero. The contracted row has power
\(N^{-m-1/2}\); its \(2m-1\) residue constants and Gaussian
give
\[
 N^{2m-1}N^{-m-1/2}N^{-(2m-1)/2}=N^{-1}.
 \tag{18}
\]
Consequently its central-sheet integral has the same original
local coefficient and action as equation (14) of the local-current
theorem. Equality of coefficients is the complex Schur Gaussian
factorization of the first private coordinate. It is not inferred
merely from equality of critical values.

For each fixed word, (17), local holomorphy and strict compact
margins give the usual small joint parameter neighborhood, both
parities, and fixed derivatives of the normalized \(O(N^{-1})\)
error. The floor in (13) is uniform; the final packet constants,
parameter neighborhood and error threshold are not asserted uniform
in word length.

The one-letter word \(4\) still has the previously proved local
current, but has no residual pair chain. It is not covered by
this main-sheet argument.

## 4. What general source propagation still requires

The reusable proposition in
[coherent prepared-cap completion](research_mixed_prepared_cap_coherent_contour_completion.md),
Section 6, now has its exact source, full-cap input, original
critical point, supporting-plane cancellation and entire main-sheet
premises for every prefix above. It does not yet have the following
word-wide comparisons:

- a coherent physical-complement bound calibrated to
  \(M_{\boldsymbol\epsilon}\), including all outer support ends;
- real outer-face and outer-alias gaps on a common deformation
  domain, together with its derivative-strip hypotheses;
- the private-alias and true-endpoint residual comparisons at
  zero outer heights required to pay the unpenalized joins.

For \(34\) these are precisely the comparisons discharged in the
completed theorem. Its elementary residual ceiling and six
successful faces cannot be attached repeatedly as independent
constants: the surrounding action and surviving boundary marginals
change. The new general main sheet does not assert those signs.

There is already a uniform source tool for the ordinary bulk.
The local estimates in
[uniform repetition](research_mixed_uniform_repetition_bound.md),
Section 2, cover a finite collection of closed typed domains:
central coherent factors, both Fourier alternatives, taper products,
zero seams and raw right-half rows. Their per-factor constants and
thresholds can be chosen independently of the word. The
[full retained-period potential](research_mixed_full_alphabet_boundary_potential.md),
equation (17), turns the established cyclic occupation inequality
into a conditional open-path bound with exact endpoint halves and
two surviving cut potentials/tangents. Those boundary terms remain
in the inequality; its reference is its specified periodic one.
For actual safe open windows, the corresponding
[finite boundary-window reduction](research_mixed_open_finite_boundary_windows.md)
keeps the literal endpoint products and their completion energies.
Neither result replaces a Fourier-ended reference by a cyclic one,
or identifies its action with a trace action.

Thus the remaining general step is a calibrated comparison of
the actual coherent cap and Fourier closing functional against
these surviving bulk boundary costs, or an operation-preserving
coherent envelope proving the same comparison. It must retain the
whole physical period and every source component. A local outgoing
packet, including the newly completed \(34\) packet, controls none
of the missing incoming-period complement by itself.

The [whole-message Schur criterion](research_mixed_paired_whole_message_schur_criterion.md)
makes one sufficient propagation estimate precise; its global
incoming envelope and off-diagonal contour bound remain additional
premises. The universal repetition and spectral bounds are bounds
for cyclic traces, not for the ordinary vector \(v(-2)\) or
the Fourier closing vector with the needed phase correlation.
This distinction is a genuine boundary obligation, rather than
unperformed enumeration of interior words.

No whole-source theorem for all prefixes, whole outgoing-period
bound, arbitrary short-filling stability or knot-family conclusion
is inferred from (17).

## 5. Why adding more fully real face tests cannot propagate this proof

There is a concrete obstruction to using the same absolute
height-zero face criterion for arbitrarily long words. It already
occurs for the all-four prefixes, whose critical points and local
currents are established above. It is an obstruction to that
source decomposition, not to their signed finite sums.

Let \(F_m\) be the full phase before contracting its first private
coordinate, and let
\[
 \zeta_*=\xi_*+i\eta_*=(s_{1,*},t_{1,*},\ldots,s_{m,*},t_{m,*}),
 \qquad M_m=\Re F_m(\zeta_*).
 \tag{19}
\]
At complete ordinary color its endpoint auxiliary has already been
eliminated by the original branch \(S(s_1)\). Along the whole
segment \(\xi_*+i\theta\eta_*\), \(0\le\theta\le1\), the
[cap curvature theorem](research_mixed_cap_upper_target_extension.md)
gives
\(-\Re(\Psi_1-g(t_1)/2)''\succeq(\pi/200)I_2\).
The residual \(R_m^{\rm a}\) has the floor \(9/46\) from
Section 3 on every such intermediate height: its pair argument
uses only absolute heights at most \(.12\), and the last Fourier
incidence remains regular and positive. These allocations cover
every coordinate. Hence
\[
             -\Re F_m''\succeq\frac3{200}I
            \quad\hbox{along that segment}.
 \tag{20}
\]
All cap heights stay inside their proved hybrid-height intervals.
This does not extend a local Hessian estimate through an unproved
source domain.

The real function \(f(\theta)=\Re F_m(\xi_*+i\theta\eta_*)\)
has \(f'(1)=0\) by original complex stationarity and
\(f''(\theta)\ge(3/200)\|\eta_*\|^2\). Integrating from the
critical endpoint therefore gives
\[
 \Re F_m(\xi_*)-M_m
       \ge\frac3{400}\|\eta_*\|^2
       >\frac{3(m-1)}{200000000}.
 \tag{21}
\]
For the last inequality, every vertex \(j\ge2\) is an ordinary
four-vertex, even the final one with its auxiliary Fourier inverse
leg. Its two full-bidisk image heights are both less than
\(-1/1000\). There are \(2(m-1)\) such legs. No asymptotic
approximation to a periodic reference is used.

Now replace only the real coordinate \(t_1=\Re t_{1,*}\) in
\(\xi_*\) by \(11/50=.22\), keeping all other real coordinates
unchanged; call the resulting point \(\xi^\partial\). It belongs
to the lower \(t_1\) face of the original independent real box.
All original support sums are strictly below one. Only the cap
and its immediately adjacent wire terms change, and on this
entire real segment
\[
 \Re\partial_{t_1}F_m
   =\log(2\sin\pi(s_1+t_1))
     +\log(2\sin\pi(t_1+s_2))
                  -3\log(2\sin\pi t_1).
 \tag{22}
\]
The original chirp has zero real derivative here.

Both sum arguments lie in \([.44,.94]\). On this interval
\(2\sin(\pi x)>1/4\), so each sum logarithm lies in
\((-3/2,1)\). For an elementary witness,
\(\sin(.06\pi)>\sin(9/50)\ge9/50-(9/50)^3/6>1/8\),
and \(e^{3/2}>1+3/2+9/8+9/16>4\).
Also \(0<\log(2\sin\pi t_1)<1\) on \(P\).
Equation (22) consequently has absolute value less than \(6\).
The displacement is less than \(.23\); the rate loss is therefore
less than \(6(.23)<2\), uniformly in \(m\).

Combining this with (21) proves the actual face-value inequality
\[
 \boxed{\quad
 \Re F_m(\xi^\partial)-M_m
             >\frac{3(m-1)}{200000000}-2.
 \quad}
 \tag{23}
\]
In particular the maximum of the uncontracted real profile on that
face cannot have a negative gap for every word length. For sufficiently
large fixed \(m\), continuity even gives a nearby supported physical
region just outside that real cut with rate above \(M_m\).

In particular the real-private-index phase envelope
\(\max_{s_1\in[.27,.49]}\Re\Psi_1(s_1,t_1)+\Re R_m(z)\)
includes this value, with \(s_1=\Re s_{1,*}\). Thus that
absolute envelope cannot repair (23) by taking more accurate
supports or by testing more faces. The discarded bulk cancellation
has an extensive rate cost. The full \(U_1\) source can still be
smaller than its real-private-index envelope, and subsequent
conditional contractions may retain the other cancellations.

Equations (17) and (23) are compatible. The first controls the
entire main sheet at its original critical heights; the second
shows why resetting an arbitrarily long source to height zero
cannot be paid by a fixed boundary displacement. A general
propagation proof must retain the coherent bulk or supply an
operation-preserving boundary estimate. No failure of a whole
finite source, knot identity or finite-exception statement is
asserted.


