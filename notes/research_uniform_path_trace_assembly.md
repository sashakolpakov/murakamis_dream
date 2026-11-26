# The geometric contribution for positive and signed circle paths

Research proof, 3 November 2026. This note belongs to the continuing
research project; the frozen manuscripts are unchanged.

For an original circle-tree presentation whose graph is a path,
the geometric point contributes with a nonzero coefficient whenever
every selected crossing power has magnitude at least eight. Signs
may differ and all auxiliary vertices may be selected. Positive
powers at least seven also suffice when the stipulated complete
outside endpoint is retained. The path and its powers are fixed
before the quantum level tends to infinity.

Section 7 proves these bounds and the resulting original Kashaev
knot limit. Sections 1--5 retain the source normalization and the
earlier threshold-sixty-four argument. The improved comparison
is still local: completing selected vertices costs less than
one tenth per incidence, whereas the corresponding original
removed rows lose more than \(21/200\) per incidence.

This does not settle the finite-exception problem. A power below
the stated threshold can remain fixed while other powers grow
through infinitely many assignments.

## 1. The exact finite source and its conventions

Let \(\Gamma=(V,E)\) be a nontrivial finite path from the original
ordered circle-tree construction. Keep its disk frames, page order
and half-twist carriers. Select a nonempty set \(I\subseteq V\).
The remaining vertices have complete boundary angle zero. Write
\[
 m=|I|,\qquad e=|E|,\qquad
 n_v=\eta_v-2p_v,\qquad |n_v|\ge64\quad(v\in I).
 \tag{1}
\]
Here \(p_v\) is the original integer filling coefficient and
\(\eta_v\) is its fixed carrier. Thus the filled primitive curve is
\(\mu_v+p_v\lambda_v^{\rm disk}\), with the original meridian and
disk longitude. No peripheral basis change is made.

For an integer level \(N\ge3\), put
\[
 q_N=e^{\pi i/N},\qquad D=N-1,\qquad
 S_j=\prod_{\nu=1}^j2\sin(\pi\nu/N),\qquad
 e_j(z)=S_j^{-2}\prod_{\nu<j}
           \bigl(2\cos((2\nu+1)\pi/N)-z\bigr).
 \tag{2}
\]
The original edge kernel and complete trace are
\[
 K_N(t,u)=\sum_{j=0}^{N-1}e_j(-2\cos t)e_j(-2\cos u),
 \qquad
 \mathcal D_{n,N}[f]=\phi_N(R^n f^\sharp),
 \quad f(t)=f^\sharp(-2\cos t).
 \tag{3}
\]
The functional \(\phi_N\) is the full Hermite trace in
\(\mathbb C[z]/(2T_N(z/2)+2)\). In particular, its double roots
retain their first normal derivatives. Define
\[
 Z_{\Gamma,I,N}=
 \left(\prod_{v\in I}\mathcal D_{n_v,N}^{(t_v)}\right)
                 \prod_{\{v,w\}\in E}K_N(t_v,t_w),
 \qquad t_w=0\quad(w\notin I).
 \tag{4}
\]
The product of traces in distinct variables is an exact finite
operation. All edge factors are multiplied before a trace is
taken; an edge shared by two selected vertices is present once.
Formula (4) is the original source obtained by composing the
circle-tree crossing and turn operations.

## 2. The stationary point and its absolute action

The edge phase is normalized by
\[
 \psi(0,0)=\frac{4G}{\pi},\qquad
 \psi_t(t,u)=-\frac1\pi
       \operatorname{arsinh}\bigl(\tan(t/2)\cos(u/2)\bigr),
 \tag{5}
\]
where \(G=\sum_{j\ge0}(-1)^j/(2j+1)^2\). Branches are continued
from \(t=u=0\). Put
\[
 \Phi(t)=\sum_{\{v,w\}\in E}\psi(t_v,t_w)
       +\sum_{v\in I}\frac{i n_vt_v^2}{4\pi}
       -i\sum_{v\in I}t_v .
 \tag{6}
\]
Corollary 3 of the
[partial-charge theorem](research_positive_path_partial_charge_bounds.md)
constructs its unique critical point in
\(|\Re t_v|\le1,\ |\Im t_v|\le1/3\). Denote it by \(t^*\).
In the range (1) it satisfies
\[
 \operatorname{sgn}(\Re t_v^*)=\operatorname{sgn}(n_v),
 \qquad |\Re t_v^*|<1/10,\qquad
                  0<-\Im t_v^*<1/200.
 \tag{7}
\]
The eight original tetrahedra on every edge are positive.
The original marked completion theorem therefore gives
\[
                 \operatorname{Vol}Y(\mathbf p)
                       =2\pi\Re\Phi(t^*),
 \tag{8}
\]
where \(Y(\mathbf p)\) is the original partial filling, with every
unselected cusp complete. All complete edge constants are included
in (6). Thus (8) fixes an absolute volume, not a variation of volume
or a value modulo logarithmic periods.

For clarity, the charge continuation used in the estimates is an
analytic family of stationary equations. It does not assume that
there is a finite quantum invariant at nonintegral charges.

## 3. A nonzero coefficient in the original trace

**Theorem 1.** For the source (4), set
\[
 \varepsilon_N=\prod_{v\in I}q_N^{\,n_vD^2/4},\qquad
 H=-\Phi''(t^*).
 \tag{9}
\]
Then, along all integer levels,
\[
 Z_{\Gamma,I,N}
   =\varepsilon_N N^{\,3(m-e)/2}
           A_{\Gamma,I}\,e^{N\Phi(t^*)}(1+O(N^{-1})),
 \tag{10}
\]
where \(|\varepsilon_N|=1\) and
\[
 A_{\Gamma,I}=
   \left(\frac{i}{\pi}\right)^m(2\pi)^{m/2}
   \frac{\displaystyle
       \prod_{v\in I}\sin t_v^*
       \prod_{\{v,w\}\in E}a_e(t_v^*,t_w^*)}
        {\sqrt{\det H}}\ne0 .
 \tag{11}
\]
The edge amplitude \(a_e\) is the one in the
[full thin-rectangle kernel theorem](research_bare_kernel_thin_rectangle.md).
The square root in (11) is the Gaussian branch on matrices with
positive definite real part. There is an expansion to every fixed
inverse-power order.

**Proof.** The original derivative sampling identity is
\[
 \mathcal D_{n,N}[f]
 =(-1)^{N-1}q_N^{\,nD^2/4}
      \sum_{j=0}^{N-1}
       \left.\frac{d}{dt}
          \left[\sin t\,f(t)e^{inNt^2/(4\pi)}\right]
          \right|_{t=\pi(N-1-2j)/N}.
 \tag{12}
\]
The [exact trace calculation](research_exact_complete_trace_contour.md)
proves this identity, including both level parities. Choose the
largest midpoint cutoff \(T_N\le19/20\). Separate (12) according
to the vertices whose grid points lie outside
\((-T_N,T_N)\).

First take the term with no outside vertices. At each vertex,
the exact residue identity replaces its retained trace by a lower
horizontal integral and a vertical integral. The horizontal
rational kernel is
\[
 \frac{e^{-iNt_v}}
       {(1-(-1)^{N-1}e^{-iNt_v})^2},
 \tag{13}
\]
and its prefactor is \(iN^2q_N^{n_vD^2/4}/\pi\).
Its leading Fourier term is exactly \(e^{-iNt_v}\), with
coefficient one. Upper and lower reflected charges have already
been combined in this identity; there is no remaining unexamined
sum of two equal-action leading terms.

Use the horizontal line at height \(\Im t_v^*\). For a vertical
term use the side with real part
\(\operatorname{sgn}(n_v)T_N\). The negative-side choice carries
its exact extra factor \(-1\). Section 6 of the
[trace comparison](research_path_mixed_trace_currents.md)
proves that every nonempty set of vertical terms has exponential
rate at most
\(\Re\Phi(t^*)-|S|/400\). It proves this for all subsets
simultaneously, with no restriction on the signs of the powers.

On every horizontal and vertical segment, the full kernel theorem
gives its uniform upper bound and its actual expansion. No wire
indices are dropped. In the all-horizontal term the edge matrices
satisfy
\[
 \Re[-2\pi\psi''(t_v,t_w)]\succeq\tfrac15 I .
 \tag{14}
\]
Their sum gives
\[
                   \Re H\succeq
               \frac1{10\pi}\operatorname{diag}(d_v)>0,
 \tag{15}
\]
where the original degrees include edges to complete vertices.
The filling quadratic has purely imaginary Hessian and does not
alter (15). The real part of the phase is strictly concave on the
whole horizontal rectangle, with its unique maximum at \(t^*\).
In particular, every fixed complement of a neighborhood of \(t^*\)
has a strict exponential gap.

Since all heights in (7) are strictly negative, replacing (13)
by its first Fourier term has an exponentially small relative
error, uniformly on the horizontal rectangle. This estimates
all higher charges together. In the resulting integral the
amplitude is
\(\prod_v\sin t_v\prod_e a_e(t_v,t_w)\). It is holomorphic
and nonzero at \(t^*\). The sine factors cannot vanish by (7).
The real Gaussian integral with complex symmetric Hessian \(H\)
is
\[
 \int_{\mathbb R^m}e^{-x^THx/2}\,dx
                 =\frac{(2\pi)^{m/2}}{\sqrt{\det H}}\ne0 .
 \tag{16}
\]
For completeness, write \(H=A+iB\), where \(A>0\) and
\(A,B\) are real symmetric. Change variables by \(A^{-1/2}\)
and diagonalize \(A^{-1/2}BA^{-1/2}\) orthogonally.
The integral becomes a product of the elementary integrals
\(\int_{\mathbb R}e^{-(1+i\beta)x^2/2}\,dx
=\sqrt{2\pi}(1+i\beta)^{-1/2}\).
This proves (16) and fixes its square-root branch.

Taylor expansion on a shrinking saddle neighborhood, dominated
by (15), now gives (11). Odd Gaussian moments vanish, and the
usual Taylor remainder estimate gives the error \(O(N^{-1})\)
and every further fixed order. The power of \(N\) is
\[
            N^{2m}\,N^{-3e/2}\,N^{-m/2}
                         =N^{3(m-e)/2}.
 \tag{17}
\]
The first factor comes from the exact trace prefactors, the
second from the full edge kernels, and the third from (16).

It remains to compare the original outside rows. Fix a nonempty
set \(S\) of vertices with such rows. Set their analytic charges
to zero and keep all other charges equal to one. The partial-charge
theorem gives a critical point with exactly those coordinates
zero. Its stationary rate exceeds the full rate by less than
\(\sum_{v\in S}d_v/800\).

The centered kernel estimate in Section 4 of the trace comparison
replaces an edge incident to a removed vertex by the same edge
phase with that coordinate zero. Its loss at each such incidence
is greater than \(1/600\). The estimate includes all derivatives
arising in (12): Markov's inequality on the fixed enlarged real
interval preserves that loss at polynomial cost. An edge with
both endpoints removed keeps both losses. At the remaining
vertices use the same exact horizontal and vertical trace
decomposition, now at the partial-charge heights.

Consequently the entire contribution for \(S\) has rate less
than
\[
                \Re\Phi(t^*)-
                          \frac1{2400}\sum_{v\in S}d_v .
 \tag{18}
\]
This comparison also holds for signed powers: their physical
crossing values have modulus one, their normal derivatives cost
only powers of \(N\), and the remaining vertical terms use the
signed comparison already proved. Each fixed path has finitely
many subsets \(S\). All are therefore exponentially smaller
than the nonzero term (11). This proves (10).
\(\square\)

## 4. The knot-complement volume identity

**Corollary 2.** Suppose every auxiliary vertex is selected,
the original strand tracing gives one main component, and there
is no internal closed component. Let \(K\) be the resulting knot
with the original carriers and integer filling coefficients (1).
Then
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|\langle K\rangle_N|
                       =\operatorname{Vol}(S^3\setminus K).
 \tag{19}
\]
The limit is over all integer levels, not a subsequence.

**Proof.** If \(\mathscr D\) is the original oriented diagram
and \(w(\mathscr D)\) is its writhe, the
[original finite-source identity](../papers/circle-tree-volume/finite-bounds.tex)
at its complete meridian gives exactly
\(\langle K\rangle_N
=q_N^{D^2w(\mathscr D)/2}Z_{\Gamma,V,N}\).
The edge insertions and physical-turn scalars equal one at
this meridian. Thus the only extra factor is the displayed
writhe unit. The component hypotheses are the ones required
by that original reduced closure.
Since a path has \(e=m-1\), (10) has polynomial prefactor \(N^{3/2}\)
and nonzero constant amplitude. Taking its absolute value,
logarithm, and then \(2\pi/N\) gives \(2\pi\Re\Phi(t^*)\).
Equation (8) is the hyperbolic volume of this original knot
complement. It proves (19). \(\square\)

The condition is on the actual crossing powers
\(|\eta_v-2p_v|\ge64\). It should not be paraphrased as a
condition on a changed continued fraction or on an unmarked
filling slope.

## 5. Boundary sources and kernels

Suppose every vertex except one endpoint is selected, and retain
that endpoint as a free boundary with angle \(u\). Then \(m=e\),
so the same original source has a nonzero holomorphic expansion
near \(u=0\) with no additional power of \(N\). Section 7 of the
trace comparison also proves the
whole-period estimate
\[
 |F_N(u)|\le C N^a
      e^{N[M-(1-\cos u)/200]},\qquad -\pi\le u\le\pi,
 \qquad M=\Re\Phi(t^*)\big|_{u=0}.
 \tag{20}
\]
It retains a quadratic bound on a small complex strip. Thus
any fixed finite collection of these paths supplies boundary
sources for the existing long-turn composition theorem, after
choosing a common smaller boundary neighborhood. Constants may
depend on the fixed path; its length does not tend to infinity
with \(N\).

There is also a two-boundary version. Let \(t_1,\ldots,t_m\)
be consecutive selected vertices, with \(|n_j|\ge64\), between
the two free endpoints \(t_0=s\) and \(t_{m+1}=u\). Define the
original kernel of this run by
\[
 \mathcal E_N(s,u)=
 \left(\prod_{j=1}^m\mathcal D_{n_j,N}^{(t_j)}\right)
                       \prod_{j=0}^m K_N(t_j,t_{j+1}).
 \tag{21}
\]

**Corollary 3.** On a fixed neighborhood of \((s,u)=(0,0)\),
\[
 \mathcal E_N(s,u)=\varepsilon_N N^{-3/2}
                     a(s,u)e^{NW(s,u)}(1+O(N^{-1})),
                      \qquad a(s,u)\ne0 .
 \tag{22}
\]
Here \(W(s,u)\) is the stationary value of the original phase
(6) with these boundary angles, and \(\varepsilon_N\) is (9).
Put \(M=\Re W(0,0)\). On the entire real boundary square,
\[
 |\mathcal E_N(s,u)|\le C N^b
       \exp N\!\left[
           M-\frac{(1-\cos s)+(1-\cos u)}{200}\right].
 \tag{23}
\]
There are also \(c,B,h>0\) such that, for real
\(|x_j|\le\pi\) and \(|y_j|\le h\),
\[
 |\mathcal E_N(x_1+iy_1,x_2+iy_2)|
 \le C_1N^{b_1}
   e^{N[M-c\sum_{j=1}^2(1-\cos x_j)+B(y_1^2+y_2^2)]}.
 \tag{24}
\]

**Proof.** The implicit function theorem and the strict error
gaps in Theorem 1 give the joint holomorphic expansion (22).
There are \(m+1\) original edges, so its power is
\(3(m-(m+1))/2=-3/2\); its nonzero amplitude is (11) at
the continued stationary point.

Apply the boundary estimate used for (20) at both exterior
incidences. Each small real boundary angle loses its square
divided by \(20\pi\) by the negative real edge Hessian.
Each large real boundary angle loses \((1-\cos u)/200\)
by the centered kernel bound. The two ranges overlap.
If a neighboring selected vertex is removed, its Markov
derivative is in that internal variable only, so both
exterior losses survive. This remains true when \(m=1\):
the two losses belong to two different incident edges.
The original discarded-row and vertical-term comparisons
therefore retain the sum of the losses, proving (23).

For completeness, the complex-strip step is genuinely
two-variable. Set \(\gamma=1/200\). The expression is an even
trigonometric polynomial of degree at most \(D=N-1\)
in each angle separately. Multiply its Laurent form by
\(z_1^Dz_2^D\exp[-N\gamma(z_1+z_2)]\) and use the maximum
principle on the unit bidisk. Equation (23) gives, after
putting \(|z_j|=e^{-|y_j|}\), the upper rate
\[
 M-2\gamma+\gamma\sum_{j=1}^2 e^{-|y_j|}\cos x_j
                         +|y_1|+|y_2|.
\]
Separate evenness permits either sign of each height.
Outside a fixed neighborhood of \((x_1,x_2)=(0,0)\),
the strip can be made thin enough to absorb the linear
height terms into half the angular loss.

Inside that neighborhood, (22)--(23) imply
\(\Re W(x)\le M-\gamma\sum_j(1-\cos x_j)\).
The stationary action is even in each boundary angle,
so its gradient vanishes at zero and
\(-\Re W''(0)\succeq\gamma I\).
Holomorphic Taylor expansion and Young's inequality
bound its mixed real-imaginary terms by
a smaller negative real quadratic plus \(B|y|^2\).
The bounded amplitude and uniform normalized error in
(22) then give (24). This proves the corollary. \(\square\)

This two-boundary result concerns runs whose selected powers
all satisfy the stated bound. An internal pair of powers
\(3,3\) has an extra incident edge compared with the proved
pendant pair; its needed kernel is not that pendant source.

## 6. Where the Fourier lower bound enters

The proof also answers precisely where the lower bound comes
from in this class. After an exact deformation of the finite
trace, rescale about \(t^*\) and normalize by its positive real
Gaussian. If \(H=A+iB\), the mean quadratic phase is
\[
 \frac{\int e^{-x^TAx/2}e^{-ix^TBx/2}\,dx}
      {\int e^{-x^TAx/2}\,dx}
 =\det(I+iA^{-1/2}BA^{-1/2})^{-1/2}\ne0.
 \tag{25}
\]
This allows nonconstant phases. It is not a positivity claim
about the coefficients of the original real state sum.
The exact contour identity gives the geometric point coefficient
one before Gaussian integration; (18) prevents the rest of the
original sum from canceling its leading term.

The next section supplies these estimates for arbitrary connected
paths at the improved thresholds. Separate pair results also
cover \(3,3\) and its mirror. An arbitrary connected group below
these thresholds is not covered by those statements; this remains
part of the obstacle to finite exceptions per template.

## 7. The source theorem at powers seven and eight

The wide finite-kernel theorem completes the geometric, current
and removed-row comparisons. We state the bound used in the
assembly before giving its exact source and marking scope.

**Established wide-kernel bound.** Put
\[
 \mathcal W=\{t:|\Re t|\le\pi/2,\ |\Im t|\le3/10\}.
 \tag{26}
\]
For the original full kernel \(\mathcal K_N(z,w)=\sum_{j<N}e_j(z)e_j(w)\),
every fixed pair of ordinary spectral derivatives has a uniform bound
\[
 \left|\partial_z^k\partial_w^\ell\mathcal K_N(z,w)
       \big|_{z=-2\cos t,\ w=-2\cos u}\right|
 \le C_{k\ell}N^{A_{k\ell}}e^{N\Re\psi(t,u)},
                  \qquad t,u\in\mathcal W,
 \tag{27}
\]
at both level parities, on the original branch of (5).
This is Theorem 3 of the
[full wide-kernel proof](research_bare_kernel_thin_rectangle.md#6-the-full-rectangle-through-real-angle-pi-over-two),
including its ordinary derivative conclusion. It is a bound
for every original index, with its actual normalization and
normal data.

That theorem also proves the nonzero holomorphic kernel expansion.
For the selected saddle, it is enough to use its previously proved
[width-one local case](research_bare_kernel_thin_rectangle.md#5-the-expansion-at-imaginary-heights-up-to-three-tenths).
The broader upper bound (27) controls the rest of the trace.

**Theorem 4 (the full path source).** The original source (4)
has the expansion (10)--(11), to every fixed
inverse-power order and along all integer levels, in either of
the following two settings:

1. Every selected power is a positive integer at least seven,
   and the path has the stipulated complete outside endpoint of
   the positive fractional-charge theorem.
2. Every selected power satisfies \(|n_v|\ge8\), with arbitrary
   signs. Any nonempty selected set is allowed, including all
   auxiliary vertices.

The amplitude in (11) is nonzero and uses the already proved
local full-kernel amplitude. All original first normals and
simple-node terms remain in the source. The expansion extends
holomorphically to a fixed neighborhood of any complete outside
colors; its ordinary spectral derivatives are obtained by
differentiating that expansion. This does not assert that a
derivative of a nonzero leading amplitude must itself be nonzero.

*Proof.* For the first setting, Theorem 5 and Corollary 7 of the
[network phase note](research_unsummed_network_phase_coercivity.md#6-a-common-central-domain-for-positive-paths-of-power-at-least-seven)
give the entire actual partial-charge family, with
\[
 |\Re t_v(\chi)|<19/20,\qquad 0\le H_v(\chi)<3/10,
 \qquad
 M(\mathbf1_S^c)-M(\mathbf1)
                   <\frac1{10}\sum_{v\in S}d_v.
 \tag{28}
\]
Here \(\mathbf1_S^c\) is zero on \(S\) and one elsewhere;
the coordinates at zero charge are exactly zero, and all their
incident edges are retained.

For the second setting, Corollary 3 of the
[signed partial-charge theorem](research_positive_path_partial_charge_bounds.md#4-signed-powers-and-filling-every-auxiliary-vertex)
constructs this family without an outside endpoint. Its bounds
give \(|t_v|\le5\pi/18<9/10\),
\(H_v\le35\pi/373<3/10\), and the same action budget
(28), since \(U_{|n|,d}/(2d)<1/10\). At positive charges
the real angle has the sign of \(n_v\), while every height
is negative. These facts also hold for each partial-charge
subset used below.

Choose the largest physical midpoint \(T_N\le\pi/2\), so
\(T_N=\pi/2+O(N^{-1})\). Split the original sampling formula
(12) by its set \(S\) of rows outside \((-T_N,T_N)\).
The strict reserve in the proofs of the
[centered incidence estimates](research_path_mixed_trace_currents.md#8-a-stronger-centered-loss-for-a-removed-incidence)
allows their removed real-angle threshold to be decreased by
a fixed positive amount, while keeping the losses \(21/200\)
and \(2(21/200)\). Indeed the modulus-entropy maximum is
continuous on the compact parameter set, its proved gap is
strict, and the full radical bound is unchanged. Ordinary
Markov inequalities apply on the correspondingly enlarged real
color interval. This covers the possible physical row between
\(T_N\) and \(\pi/2\), at both parities.

First take \(S=\varnothing\). Apply the exact Hermite contour
identity (15) of the trace-comparison note at every vertex.
Use the lower horizontal heights \(-H_v\) and the vertical
side \(\operatorname{sgn}(n_v)T_N\). The negative-side choice
retains its extra factor \(-1\); a mixed subset of vertical
sides therefore carries exactly \(\prod_v\operatorname{sgn}(n_v)\)
over that subset. The principal horizontal charge is still
\(+1\) at each vertex, for either sign of \(n_v\).

For positive powers, Theorem 6 of the
[mixed-current note](research_path_mixed_trace_currents.md#9-vertical-current-monotonicity-at-powers-of-at-least-seven)
bounds every nonempty vertical subset by \(M-|S'|/80000\).
Its proof also applies to the signed case. At a side
\(t_v=\sigma_vT_N+ih\), the filling derivative is
\(-|n_v|T_N/(2\pi)\). When \(h\le0\),
\(\Im\tan(t_v/2)\le0\), irrespective of \(\sigma_v\),
and a positive imaginary return satisfies
\[
 \sin(\Im r_{vw})
 \le |\Re\tan(t_v/2)|\,|\Im\cos(t_w/2)|<4/35.
 \tag{29}
\]
The principal asinh branch has \(|\Im r|<\pi/2\), even
when its real part is negative. Thus the same height derivative
is less than \(-1/40\). Above zero height the bound
\(\Im r<\pi/2\) again suffices. The wider edge Hessian
bound \(\Re K\succeq I/10\) holds for all signs of the
real and imaginary coordinates. It gives the same bottom-face
loss, since
\(|\sigma_vT_N-\Re t_v^*|=T_N-|\Re t_v^*|>1/25\).
This proves the mixed-current comparison in both settings.

The established bound (27) turns those phase bounds into bounds for the
actual finite integrands. The all-horizontal phase is strictly
concave, with its unique maximum at \(t^*\). Every saddle
coordinate is strictly inside the proved width-one local kernel
domain. The principal rational trace coefficient is exactly one,
and all its higher Fourier charges are exponentially smaller.
Consequently the local Gaussian computation (14)--(17) applies
unchanged, with the weaker but sufficient bound
\(\Re[-\Phi''(t^*)]\succeq\operatorname{diag}(d_v)/(20\pi)\).
It gives exactly (10)--(11), including their power of \(N\),
unit scalar and nonzero determinant.

Now fix a nonempty outside-row subset \(S\). Keep its literal
physical values, crossing phases and first normals. Deform the
remaining exact traces at the stationary heights for
\(\chi=\mathbf1_S^c\), before taking any modulus bounds.
On an edge incident to one removed vertex, the centered bound
replaces its exponent by \(\Re\psi(0,t_w)-21/200\).
For two removed endpoints the exponent is
\(M_\infty-2(21/200)\). These estimates include every
ordinary derivative produced by the removed first normals.
The crossing values have modulus one on those real rows;
their derivatives and the finite row weights cost only powers
of \(N\), for the fixed integer powers.

The remaining exponent is therefore precisely the original
phase with those vertices fixed at zero, minus
\((21/200)\sum_{v\in S}d_v\). Apply (27) and the same horizontal
and mixed-current comparisons to this partial-charge source.
Equation (28) gives the strict total bound
\[
 \operatorname{rate}(S)
 < M(\mathbf1)-\frac1{200}\sum_{v\in S}d_v.
 \tag{30}
\]
When no selected vertex remains, the stationary action is the
sum of the retained complete-edge constants and the same
calculation applies without a contour integral. All subsets
and normal-product terms are finite in number before
\(N\to\infty\). None can cancel the nonzero Gaussian term.

The estimates have strict gaps and apply to actual holomorphic
edge functions. A small complex perturbation of the complete
outside colors preserves them; the implicit function theorem
continues the saddle inside the local kernel domain. The
resulting holomorphic expansion has the claimed ordinary
spectral derivatives. This proves the theorem. \(\square\)

The marked action-volume identity remains (8) in both settings:
the positive charge family supplies it in the first, and the
signed marked-completion theorem supplies it in the second.

**Corollary 5 (the original knot invariant).** Select every
auxiliary vertex, retain the original carriers and slopes
\(n_v=\eta_v-2p_v\), and suppose \(|n_v|\ge8\).
If the original strand tracing gives one main component and
no internal closed component, its resulting knot \(K\) satisfies
\[
 \lim_{N\to\infty}\frac{2\pi}{N}\log|\langle K\rangle_N|
                    =\operatorname{Vol}(S^3\setminus K).
 \tag{31}
\]
The limit is along all integer levels.

*Proof.* The exact original source identity in Corollary 2 changes
\(Z_{\Gamma,V,N}\) only by its writhe unit. Since \(e=m-1\),
Theorem 4 gives the nonzero prefactor \(N^{3/2}A_{\Gamma,V}\)
and exponential rate \(\Re\Phi(t^*)\). The signed marked
completion identifies \(2\pi\Re\Phi(t^*)\) with the absolute
hyperbolic volume of this original knot complement. Taking the
logarithm proves (31). \(\square\)

These are the stated families of original marked presentations.
They do not assert finitely many exceptions for arbitrary
templates. The positive power-seven statement retains its
complete outside endpoint; it is not an all-selected
power-seven knot theorem.
