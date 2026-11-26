# The full bare kernel at a positive power-three path point

Research note, 3 November 2026. The full original bare edge kernel does
not have its geometrically selected packet throughout the positive
domain needed by paths with powers at least three. At an explicit
positive homogeneous degree-two, power-three point, its high Newton
endpoint is the leading term, and the entire lower half is
exponentially smaller. This holds at both level parities and on a fixed
complex neighborhood, with ordinary boundary derivatives retained.
The point is also approached by actual internal edges of finite
power-three paths with complete outside ends. This is an obstruction
to factoring a general short-path proof into bare geometric edge
packets; it is not a counterexample to the original full-source volume
conjecture.

## 1. Exact reflection and a high-half estimate

Write
\[
 D=N-1,\quad c_j=2\cos((2j+1)\pi/N),\quad
 S_j=\prod_{r=1}^j2\sin(\pi r/N),\quad
 e_j(z)=S_j^{-2}\prod_{r<j}(c_r-z),
 \qquad K_N(z,w)=\sum_{j=0}^D e_j(z)e_j(w).
 \tag{1}
\]
Here the arguments of the angular kernel are related by
\(z=-2\cos t,w=-2\cos u\). These are the original ordinary
polynomials, without spectral reduction. In particular their first
normal derivatives at repeated roots remain present.

The exact reflection used in the
[terminal endpoint-sector theorem](research_three_crossing_kernel_and_boundary_tail.md),
equation (13), gives
\[
 \frac{e_{D-r}(z)}{e_D(z)}
       =\frac{S_r^2}{\prod_{a=1}^r(c_a-z)},\qquad
 e_D(z)=\frac{(-1)^D P_N(z)}{N^2(z-c_0)},\qquad
 P_N(z)=2T_N(z/2)+2.
 \tag{2}
\]
It follows directly from \(S_rS_{D-r}=N\) and \(c_{D-a}=c_a\).

**Lemma 1.** Let \(m_N=\lfloor D/2\rfloor\). On every compact
subset of \(\{|\Im z|>1,\ |\Im w|>1\}\),
\[
 \sum_{r=0}^{m_N}e_{D-r}(z)e_{D-r}(w)
   =e_D(z)e_D(w)\{1+O(N^{-4})\}.
 \tag{3}
\]
Every fixed mixed derivative of the relative error is also
\(O(N^{-4})\), locally uniformly.

*Proof.* Work first on a slightly larger compact neighborhood and put
\(R=\inf|\Im z|\inf|\Im w|>1\). By (2), the absolute value of
the \(r\)-th relative summand is at most \(S_r^4R^{-r}\).
Throughout \(r\le m_N\), one has \(S_r^2\le2N\): the consecutive
ratios first decrease and then increase, and the final value is at
most \(2N\). Choose a fixed \(0<\delta<1/4\) such that
\(16\sin^4(\pi\delta)<R/2\). For \(1\le r\le\delta N\),
\[
 S_r^4R^{-r}\le(S_1^4/R)2^{1-r}=O(N^{-4})2^{1-r}.
 \tag{4}
\]
For the other indices the bound \(4N^2R^{-r}\) is exponentially
small. Summing proves (3); Cauchy's formula proves the derivative
claim. All zeros of \(e_D\) are real, so the relative errors are
holomorphic on the neighborhood used. \(\square\)

## 2. An exact positive point with the original unit charge

Set
\[
 z_*={1-3\sqrt3\,i\over2},\qquad
 t_*=a-iH=\arccos\!\left(-{1\over4}
                              +{3\sqrt3\over4}i\right),
 \quad 0<a<\pi, H>0.
 \tag{5}
\]
Then
\[
 \cosh^2H={11+3\sqrt{13}\over8},\quad
 \sinh^2H={3+3\sqrt{13}\over8},\quad
 {\pi\over2}<a<{2\pi\over3},\qquad H>1.
 \tag{6}
\]
Indeed \(\cos a\cosh H=-1/4\) and
\(\sin a\sinh H=3\sqrt3/4\) give the first two identities.
The angle bounds follow from \(-1/4<\cos a<0\).
For the last assertion, \(\sinh1<5/4\), whereas
\((3+3\sqrt{13})/8>25/16\).

**Lemma 2.** This point is in the original positive edge domain, and
its complete-point branches satisfy the unexponentiated equation
\[
          3t_*+4i\operatorname{arsinh}(\sin(t_*/2))=2\pi.
 \tag{7}
\]
Thus it is the homogeneous unit-charge stationary point for a
degree-two vertex of power three.

*Proof.* Put \(v=\tan(t_*/2)\), and use the canonical square root
\(q=\sqrt{1+2v^2}\). Exact algebra gives
\[
 v^2=-\frac13-\frac{2i}{\sqrt3},\quad
 q=\frac2{\sqrt3}-i,\qquad
 (\Re q)^2-2(\Re v)^2=\frac{5-\sqrt{13}}3>0.
 \tag{8}
\]
The [original positive-edge criterion](research_positive_edge_global_monotonicity.md),
Theorem 1, therefore makes all eight original tetrahedra strictly
positive. It also selects these branches, rather than just a solution
of an exponentiated relation.

For an explicit logarithmic calibration, let
\(r=\operatorname{arsinh}(\sin(t_*/2))\) on the principal branch.
The argument has positive real and negative imaginary parts, so
\(\Re r>0\) and \(-\pi/2<\Im r<0\).
Writing \(v_0=e^{it_*/2}\), the identity
\(2\cos(t_*/2)=(3+i\sqrt3)/2\) implies
\[
 v_0^3+v_0^{-3}-(v_0^2+v_0^{-2})+4=0.
 \tag{9}
\]
Consequently \(e^{2r}\) is one of \(-v_0^3,-v_0^{-3}\).
Its modulus exceeds one, which selects \(-v_0^3\). Since
\(3a/2-\pi\in(-\pi/4,0)\), the principal argument fixes
\[
             r=\frac{3H}{4}+i\left(\frac{3a}{4}-\frac\pi2\right).
 \tag{10}
\]
This is (7), with no remaining logarithmic integer. The positive
edge branch agrees with the principal return: its real and imaginary
parts have the displayed ranges, and the positive-domain return
map is the continuation of the original complete branch.
\(\square\)

## 3. The full kernel has a different exponential rate

**Theorem 3.** On some fixed complex neighborhood of \((z_*,z_*)\),
\[
       K_N(z,w)=e_D(z)e_D(w)\{1+O(N^{-4})\},
 \tag{11}
\]
with the same estimate for every fixed mixed derivative of the
relative error. In particular, along the full sequence of integer
levels,
\[
        \lim_{N\to\infty}\frac1N\log|K_N(z_*,z_*)|=2H.
 \tag{12}
\]
The geometrically selected edge phase has strictly smaller real part:
\[
             \Re\psi(t_*,t_*)
                    <\frac43+\frac H4<2H.
 \tag{13}
\]

*Proof.* Lemma 1 handles the high half. For its complementary indices
\(0\le j<D-m_N\), one has \(j\le N/2\). On the physical real
spectral interval,
\[
 \max_{c\in[-2,2]}|c-z_*|=\sqrt{13}.
 \tag{14}
\]
Let \(\mathcal J(x)=\int_0^x\log(2\sin\pi s)\,ds\).
The uniform sine-factorial estimate is
\(\log S_j=N\mathcal J(j/N)+O(\log N)\), including its ends.
Its minimum is \(\mathcal J(1/6)=-c/2\), where
\[
 c=2\mathcal J(5/6)<1/3
 \tag{15}
\]
by the elementary series estimate in
[the next-step source theorem](research_three_crossing_next_step_profile.md),
Lemma 3. Hence
\[
 \sum_{j<D-m_N}|e_j(z_*)|^2
   \le CN^A\exp\!\left[N\left(\tfrac12\log13+2c\right)\right],
 \qquad \tfrac12\log13+2c<2.
 \tag{16}
\]
For the last strict inequality, \(\log13<8/3\): already
\(\sum_{r=0}^5(8/3)^r/r!=49621/3645>13\).
In contrast, (2) and
\[
       P_N(-2\cos t)=2+2(-1)^N\cos(Nt)
 \tag{17}
\]
show that \(N^{-1}\log|e_D(z_*)|\to H>1\).
Thus (16) is exponentially smaller than the leading high-half term.
All inequalities are strict and persist on a small product
neighborhood; the same factorial bound with
\(\max_{c\in[-2,2]}|c-z|\) proves its uniform version there.
This gives (11), followed by the derivative claim by Cauchy's formula.
The signs in (17) change with level parity, but its unique growing
exponential does not disappear at either parity.

For comparison with the actual geometric branch, write
\(g=\Im r=(3a-2\pi)/4\). The
[absolute positive-edge volume identity](research_positive_edge_volume_identity.md)
gives
\[
 V_e=2\pi\Re\psi(t_*,t_*)+4Hg,
 \qquad V_e\le8G.
 \tag{18}
\]
The volume bound follows from \(V_e=8G-8(E_P+E_Q)\) and
nonnegativity of the convex square energy. Since \(a>\pi/2\),
\[
 \Re\psi(t_*,t_*)
 \le\frac{4G}{\pi}+\frac{H(2\pi-3a)}{2\pi}
 <\frac43+\frac H4<2H.
 \tag{19}
\]
Here \(G<1,\pi>3,H>1\) suffice. This also gives an open
neighborhood on which the full bare-kernel rate is strictly greater
than the geometric phase rate. \(\square\)

More generally, put
\(R(z)=\max_{c\in[-2,2]}|c-z|\) and
\(\ell(z)=\log|\zeta(z)|\), where
\(\zeta+\zeta^{-1}=z\) and \(|\zeta|>1\). The same proof gives
(11), uniformly on compact subsets of the explicit open region
\[
 |\Im z|>1,\quad |\Im w|>1,\qquad
 \ell(z)+\ell(w)>\tfrac12\log(R(z)R(w))+2c.
\]
Thus endpoint dominance is an open regime of the original kernel,
not a vanishing or phase coincidence peculiar to the algebraic point.

The proof establishes actual dominance in the original complex sum.
It is stronger than comparing a single summand's absolute value with
the geometric action: the rest of the high half is relatively
\(O(N^{-4})\), and the whole low half is exponentially smaller.
For orientation only, the exact point has
\(t_*\approx1.72277-1.08707i\); no numerical estimate enters the
strict comparisons above.

The leading endpoint is also visible in the original Hermite algebra.
It obeys \(e_D(c)=0\) at every physical root, including the simple
root \(-2\) when \(N\) is odd. Its first normal vanishes at every
double root except \(c_0\), where
\[
                 e_D'(c_0)=\frac{(-1)^D}{4\sin^2(\pi/N)}.
\]
Indeed \(P_N''(c_0)=N^2/(2\sin^2(\pi/N))\), so this follows
from (2). Thus a value-only spectral transform would erase precisely
the mode which dominates here. This endpoint contribution cannot be
dropped from the original full Hermite source; its later contraction
must be assessed with the original first-normal trace.

## 4. The obstruction occurs on finite selected paths

**Corollary 4.** Consider finite selected paths of increasing length,
all of whose powers are three, with a complete outside vertex at
each end. Their actual positive unit-charge solutions have internal
edge pairs approaching \((t_*,t_*)\). More precisely, a selected
internal edge can be chosen at distance \(O(m^{-1/2})\) from that
pair, where \(m\) is the number of selected vertices. Therefore
some finite paths already contain an actual edge on which the full
bare-kernel geometric packet is false. The mirrored statement holds
for powers minus three.

*Proof.* Use the square angle coordinates and energy
\(\mathcal E=4\sum_e(E_{P,e}+E_{Q,e})\) from the
[convex filling variation](research_positive_filling_convex_variation.md).
The [integer corridor interiority theorem](research_negative_corridor_variational_bounds.md),
Theorem 15, and its mirror supply the unique positive minimizer for
each of these finite paths, with the literal outside conditions.

The homogeneous reference assigns \(s=a\) and \(g=(3a-2\pi)/4\)
at every incidence, including the two outside endpoints temporarily.
It satisfies every selected equation
\(\sum g-3s/2=-\pi\). Make a feasible trial by replacing the two
outside values by \(s=g=0\), leaving every selected value and
incidence unchanged. On an attaching edge its two square coordinates
are, up to the orientation convention,
\[
          (A_P,y_P)=(a/4,g/2),\qquad
          (A_Q,y_Q)=(a/4,g/2).
 \tag{20}
\]
They are strictly inside the square. The homogeneous internal edges
are positive by Lemma 2. Thus the trial energy differs from the
homogeneous reference energy by a constant independent of \(m\).

Let \(X^*\) denote the same homogeneous reference on all edges.
The quadratic supporting inequality proved in
[the quantitative volume comparison](research_positive_edge_volume_identity.md),
equation (39), applies separately at each of its fixed interior squares:
\[
 \mathcal E(X)\ge\mathcal E(X^*)+
           d\mathcal E_{X^*}(X-X^*)+\kappa\|X-X^*\|_2^2,
 \qquad \kappa>0,
 \tag{21}
\]
uniformly on the entire product of closed squares. The constant is
independent of path length, since the reference square coordinates
are fixed in the interior.

At the reference \(h_*=-H\), \(k_*=3H/4\). For each selected
vertex the linear term is
\[
        2k_*\Delta s+h_*\sum\Delta g
        =H\left(\tfrac32\Delta s-\sum\Delta g\right)=0.
 \tag{22}
\]
Only the two outside terms remain. Each is
\(-k_*a+h_*(g_{\rm out}-g)\), and its magnitude is bounded
independently of \(m\), since every incidence \(g_{\rm out}\)
belongs to \([-\pi/2,\pi/2]\). Compare (21) for the actual
minimizer with the feasible trial upper bound. It follows that
\[
                       \|X-X^*\|_2^2\le C
 \tag{23}
\]
with \(C\) independent of \(m\). Among the \(m-1\) internal
edges there is therefore one whose two squares differ from their
reference by \(O(m^{-1/2})\). The inverse square map and its
gradient are smooth near the fixed interior reference. They recover
the actual complex angles on this edge, proving the asserted
convergence. The open-neighborhood conclusion of Theorem 3 now
applies for all sufficiently long paths. Complex conjugation and
\(t\mapsto-\overline t\) give the negative-power statement.
\(\square\)

This argument concerns the actual partial-filling solutions and their
original edges; it does not use an infinite path as a substitute for
a finite template. The usual carrier, primitive-slope and topological
eligibility hypotheses remain necessary when interpreting a chosen
path as a specified link exterior. No assertion about cancellation in
its fully contracted quantum source follows. Rather, a proof at these
small powers must retain and group the endpoint sector with the
original trace/crossing operations, or change the exact source chart.
The thin-rectangle packet used for large powers remains unaffected.

## 5. Removing the radical still leaves a larger cutoff current

Let \(m=\lfloor N/2\rfloor\) and \(L=D-m\). The exact low kernel
after removal of the full physical radical is
\[
          K_N^{\rm low}(z,w)=\sum_{j=0}^{L}e_j(z)e_j(w).
 \tag{24}
\]
At odd levels this retains the middle polynomial \(e_m\), which
does not belong to the radical. See
[the full radical contraction](research_high_newton_radical_contraction.md).
This sharply truncated kernel also fails to have the geometric
packet on a neighborhood of \((t_*,t_*)\). The following argument
uses its exact cutoff equation; it does not assert a pointwise
asymptotic for (24).

First strengthen the strict phase comparison to
\[
          H-\Re\psi(t_*,t_*)>\frac{443}{6400\pi}>0.
 \tag{25}
\]
Here is an elementary proof, without a dilogarithm enclosure.
Write \(g=(3a-2\pi)/4\). The two square energies at the homogeneous
point are equal, by the evenness and interchange symmetry of the
square energy. They are \(E(A,y)\), with
\[
                A=\frac{2\pi-a}{8},\qquad
                y=\frac{5a-2\pi}{8}.
 \tag{26}
\]
For \(0<A,y<\pi/4\), the explicit square derivative gives
\[
 E(A,y)=E(0,y)+\frac12\int_0^A
             \operatorname{arsinh}(\tan(2v)\cos(2y))\,dv
 \ge\frac{y^2+\cos(2y)A^2}{2}.
 \tag{27}
\]
Indeed \(\operatorname{arsinh}(\tan s)\ge s\) for
\(0\le s<\pi/2\), and concavity of \(\operatorname{arsinh}\) on
the positive real axis gives
\(\operatorname{arsinh}(b\tan s)\ge
b\operatorname{arsinh}(\tan s)\) for \(0\le b\le1\).

The exact expression in (6) implies
\(3/2<\cosh H<7/4\). Thus
\(a=\pi/2+\arcsin(1/(4\cosh H))\) obeys
\[
 \frac{17}{10}<a<\frac74,\qquad
 A>\frac9{16},\qquad \frac14<y<\frac{11}{32},\qquad
 \cos(2y)>1-\frac12(11/16)^2>\frac34.
 \tag{28}
\]
For the upper angle bound, use
\(\arcsin(1/6)<17/100\), which follows from
\(\sin(17/100)\ge17/100-(17/100)^3/6>1/6\), and
\(\pi/2<11/7\). For the lower bound use
\(\pi/2>157/100\) and \(\arcsin(1/7)>1/7\).
The bounds on \(A,y\) then follow from \(3<\pi<22/7\), using
\(\pi>157/50\) for the displayed bound on \(A\).
Consequently \(E(A,y)>307/2048\). The alternating series through
\(1/169\) gives \(G<23/25\), so the actual edge volume satisfies
\[
 V_e=8G-16E(A,y)<\frac{15877}{3200},\qquad
                              3aH>\frac{51}{10}.
 \tag{29}
\]
Using (18),
\(H-\Re\psi=(3aH-V_e)/(2\pi)\), proves (25).

For the exact finite identity, let \(\mathscr L_N\) be the
original Askey--Wilson difference operator in the angular variable:
\[
 \begin{split}
 (\mathscr L_N F)(t)&=-A_N(t)F(t-2\theta)
    +(c_0+A_N(t)+C_N(t))F(t)-C_N(t)F(t+2\theta),\\
 A_N(t)&=\frac{4\cos^4((t-\theta)/2)}
                    {\sin t\sin(t-\theta)},\qquad
 C_N(t)=A_N(-t).
 \end{split}
 \tag{30}
\]
The [exact off-grid difference calculation](research_edge_kernel_difference_and_endpoint_bound.md),
equation (8), proves
\(\mathscr L_N e_j=c_j e_j-s_j^2e_{j-1}\), where here
\(e_j(t)=e_j(-2\cos t)\) and the last term is zero for \(j=0\).
Together with
\(we_j(w)=c_j e_j(w)-s_{j+1}^2e_{j+1}(w)\), it telescopes to
\[
 (w-\mathscr L_N^{(t)})K_N^{\rm low}(-2\cos t,w)
        =-s_{L+1}^2 e_L(-2\cos t)e_{L+1}(w).
 \tag{31}
\]
This is an exact ordinary polynomial identity, with all boundary
normals retained. There is no discarded endpoint or division by a
spectral value.

At the diagonal the right side simplifies at both parities:
\[
 -s_{L+1}^2e_L(z)e_{L+1}(z)=
 \begin{cases}
    4P_N(z)/[N^2(z-c_{m-1})],&N=2m,\\[1mm]
    P_N(z)/N^2,&N=2m+1.
 \end{cases}
 \tag{32}
\]
To verify this, at even levels the distinct-root product squares to
\(P_N\) and \(S_m^2=2N\), so \(e_m^2=P_N/(4N^2)\).
At odd levels \(P_N=(z+2)\prod_{a<m}(z-c_a)^2\) and
\(S_m^2=N\), so \(e_m^2=P_N/[N^2(z+2)]\).
The one-step Newton relation gives exactly (32), including its sign.
The even expression has a removable singularity at its displayed
physical node; no such issue occurs near \(z_*\).

**Theorem 5.** No fixed neighborhood of \((t_*,t_*)\) admits a
uniform estimate of the form
\[
 |K_N^{\rm low}(-2\cos t,-2\cos u)|
            \le CN^B e^{N\Re\psi(t,u)}.
 \tag{33}
\]
In particular it cannot admit the geometric saddle packet with a
nonzero analytic amplitude. More concretely,
\[
 \liminf_{N\to\infty}\frac1N\log
  \max_{\epsilon\in\{-1,0,1\}}
  |K_N^{\rm low}(-2\cos(t_*+2\epsilon\pi/N),z_*)|\ge H.
 \tag{34}
\]

*Proof.* The coefficients in (30) are uniformly bounded on a fixed
neighborhood of \(t_*\): \(\sin t_*\ne0\), and
\(\theta\to0\). By (17) and (32), the absolute value of the
right side of (31), at \(t=t_*\), \(w=z_*\), is bounded below by
\(cN^{-2}e^{NH}\) for all sufficiently large \(N\), at both
parities. The triangle inequality in (31) therefore proves (34).
If (33) held, holomorphy of the original geometric phase would give
\[
 \Re\psi(t_*+2\epsilon\pi/N,t_*)
                         =\Re\psi(t_*,t_*)+O(N^{-1}),
\]
so its left side would have rate at most \(\Re\psi(t_*,t_*)\).
This contradicts (25). \(\square\)

The obstruction persists on an open neighborhood of the pair.
Indeed the same even and odd product identities show that both
\(e_L(z)\) and \(e_{L+1}(z)\) have rate \(\ell(z)/2\), uniformly
near \(z_*\). The forcing in (31) therefore has rate
\((\ell(z)+\ell(w))/2\), which remains strictly larger than the
geometric rate near \((z_*,z_*)\). Corollary 4 thus also supplies
actual finite selected-path edges where a uniform packet for the
radical-removed kernel fails.

This argument proves a surviving finite cutoff current and a
microscopic three-point lower bound. It does not claim the full
pointwise asymptotic of \(K_N^{\rm low}(z_*,z_*)\), nor does it
claim that the cutoff current survives the remaining original
network trace. The radical matching contraction and the complementary
low-kernel contour must be combined with that current retained.
In particular, (31) can be contracted with the remaining original
vertex functionals before estimating its terms. A geometric packet
for that joint low trace is compatible with everything proved here;
the obstruction only rules out replacing its individual low kernels
by geometric packets on this domain.

## 6. The midpoint forcing after the original internal-pair trace

The forcing in (31) can be small after its original traces even
though it obstructs an individual bare-kernel packet. This section
proves that fact for the internal pair with two complete outside
ends. It retains the first repeated middle node at even levels.

For a canonical algebra element
\(F=\sum_{j=0}^D F_j e_j\), put
\(\|F\|_{\rm val}=\max_{P_N(c)=0}|F(c)|\). Recall
\(m=\lfloor N/2\rfloor\), \(L=D-m\), and set
\(s_j=2\sin(j\pi/N)\).

**Lemma 6.** At odd levels,
\[
       |\phi_N(e_LF)|=|F_m|\le N\|F\|_{\rm val}.
 \tag{35}
\]
At even levels \(N=2m\ge4\), set \(c_*=c_{m-1}\). Then
\[
       |\phi_N(e_LF)|=|F_m|
                   \le2N^2\|F\|_{\rm val}+4|F'(c_*)|.
 \tag{36}
\]
At either parity,
\[
        |\phi_N(e_{L+1}F)|=|F_{m-1}|
                                      \le N\|F\|_{\rm val}.
 \tag{37}
\]

*Proof.* The identities with coefficients follow from the original
pairing \(\phi_N(e_i e_j)=\delta_{i+j,D}\). At odd levels the
nodes through \(c_m=-2\) are distinct, so (35) is precisely the
[last distinct-node coefficient bound](research_original_low_color_bound.md),
equations (13)--(15), applied to arbitrary \(F\).
Equation (37) follows from \(|b_{m-1,a}|\le2\) in
[the radical contraction](research_high_newton_radical_contraction.md)
and \(2m\le N\).

For clarity, the even coefficient admits the following exact
first-normal formula. Write
\[
 E=e_{m-1}(c_*)=\frac2{s_1},\qquad
 T=\sum_{a=0}^{m-2}\frac1{c_*-c_a},\qquad \eta=(-1)^D.
 \tag{38}
\]
Then
\[
 \begin{split}
 F_m={}&\sum_{a=0}^{m-2}
       \frac{4b_{m-1,a}}{c_*-c_a}F(c_a)\\
 &+\eta E\bigl[(s_1^2T-c_*)F(c_*)+s_1^2F'(c_*)\bigr].
 \end{split}
 \tag{39}
\]
Indeed \(e_m(z)=(c_*-z)e_{m-1}(z)/4\). At every other
physical node, this and the radical trace formula express
the surviving normal coefficient as
\(4b_{m-1,a}/(c_*-c_a)\). At \(c_*\), the ordinary product
gives \(e_{m-1}'(c_*)=ET\), and the exact physical residue is
\(\eta[(4-c_*^2)h'(c_*)-c_*h(c_*)]\), with
\(4-c_*^2=s_1^2\). This proves (39).
The value \(E=2/s_1\) follows from the distinct-node Newton
product, \(S_{m-1}^2=N/2\), and \(S_{N-2}=N/s_1\).

The physical root gaps obey
\[
 c_a-c_*\ge\frac{16(m-1-a)^2}{N^2},\qquad
 |T|<\frac{N^2}{8}.
 \tag{40}
\]
This is the sine chord bound in the difference of cosines, followed
by \(\sum_{d\ge1}d^{-2}<2\). Thus the total absolute weight in
the first line of (39) is less than \(N^2\).
Also \(4/N\le s_1\le2\pi/N\), so
\[
 E\le N/2,\qquad s_1^2|T|<\pi^2/2<5,\qquad
 E s_1^2=2s_1\le4.
 \tag{41}
\]
The central value coefficient is therefore at most \(7N/2\).
For even \(N\ge4\), \(N^2+7N/2\le2N^2\). These estimates in
(39) give (36). \(\square\)

For fixed signed integers \(n,p\), retain the original two outside
spectral variables \(z_u=-2\cos u,z_v=-2\cos v\). The traced
right side of (31) is exactly
\[
 \mathscr J_{n,p,N}(u,v)
   =-s_{L+1}^2\,
       \phi_N\!\left(R^n e_L K_N(\,·\,,z_u)\right)
       \phi_N\!\left(R^p e_{L+1}K_N(\,·\,,z_v)\right).
 \tag{42}
\]
All crossing units and the actual ordinary boundary polynomials
remain in this expression.

**Theorem 7.** For arbitrary fixed signed \(n,p\), uniformly over
real \(u,v\in[-\pi,\pi]\),
\[
 |\mathscr J_{n,p,N}(u,v)|\le C_{n,p}N^A
  \exp N\left[2M_\infty-
       \frac{(1-\cos u)+(1-\cos v)}{200}\right].
 \tag{43}
\]
After dropping the two real losses, every fixed pair of ordinary
boundary derivatives satisfies the corresponding bound. More
generally, on each fixed complex angular strip,
\[
 |\partial_{z_u}^{r}\partial_{z_v}^{s}
                  \mathscr J_{n,p,N}(u,v)|
 \le C_{n,p,r,s}N^{A_{r,s}}
                e^{N[2M_\infty+|\Im u|+|\Im v|]}.
 \tag{44}
\]
In particular the complete-boundary forcing has rate at most
\(2M_\infty\).

*Proof.* For a fixed real outside angle, let
\(S(u)=\sup_{x\in[-2,2]}|K_N(x,z_u)|\). The
[two-real kernel bound](research_path_mixed_trace_currents.md),
equation (21), gives
\[
            S(u)\le CN^a
                  e^{N[M_\infty-(1-\cos u)/200]}.
 \tag{45}
\]
Its outside-angle loss is independent of the internal variable.
Consequently Markov's polynomial inequality in that internal
variable preserves the loss and gives
\(\sup_x|\partial_xK_N(x,z_u)|\le D^2S(u)/2\).

The crossing has \(|R(c_a)^n|=1\) at all physical nodes.
At the even middle double node its original first normal is
\[
       (R^n)'(c_*)/R(c_*)^n=\frac{in}{2s_1},
                  \qquad |(R^n)'(c_*)|\le |n|N/8.
 \tag{46}
\]
This is the \(m_j=1\) case of the
[full crossing normal](research_all_color_path_normal_bound.md),
equation (3), and holds for negative powers as well.
Using (35)--(37), Markov's bound, and (46), we obtain at both parities
\[
 \begin{split}
 \left|\phi_N(R^n e_LK_N(\,·\,,z_u))\right|
       &\le(4+|n|/2)N^2S(u),\\
 \left|\phi_N(R^p e_{L+1}K_N(\,·\,,z_v))\right|
       &\le N S(v).
 \end{split}
 \tag{47}
\]
Since \(s_{L+1}^2\le4\), (43) follows. This proof uses only
physical values and the explicitly retained central normal; it
does not evaluate individual high Newton polynomials on a complex
internal contour.

For completeness, the derivative and strip extension is elementary.
If a polynomial \(P(z)\) of degree at most \(D\) is bounded by
\(S\) on \([-2,2]\), its Chebyshev coefficients are at most
\(2S\). At \(z=-2\cos u\),
\[
        |\partial_z^rP(z)|
            \le C_r N^{2r+1} e^{D|\Im u|}S.
 \tag{48}
\]
One may check this directly: the derivative of \(T_j(z/2)\)
has nonnegative Chebyshev coefficients up to the harmless signs
from \(z=-2\cos u\), their total absolute mass is at most
\(j^{2r}\), and every involved frequency is at most \(j\).
Apply (48) successively to the two outside variables of (42),
using the uniform real bound (43) with its losses dropped.
The degrees are at most \(D\) in each variable. This proves (44),
including ordinary normals at the complete boundary. \(\square\)

For the internal pair \(n=p=3\), the
[strict pair-energy comparison](research_radical_path_sector_gap.md),
Theorem 4, proves \(M_{3,3}>2M_\infty+1/100\). Hence (42) has a
strict exponential gap below that actual geometric rate, at both
parities. The gap persists on a sufficiently small complex
two-boundary neighborhood, by (44) and holomorphic continuation of
the geometric action. The same statement holds for the mirrored
pair. Thus both the full radical sector and this entire midpoint
forcing are controlled after their literal original traces.

This does not determine the homogeneous solution or its leading
coefficient in a joint low-sector asymptotic. It supplies a bounded
inhomogeneous term for that remaining source problem; no bare-kernel
packet has been substituted for the traced low kernel.

The [full radical contraction theorem](research_high_newton_radical_contraction.md)
now gives an exact way to do this grouping. The entire nilpotent
high-index sector contracts to physical evaluations with polynomial
weights, and its simultaneous insertions are indexed by graph
matchings. Every remaining edge coupling is kept. This removes
the need to estimate those modes at an off-grid geometric point,
but leaves the physical-color source bounds and their strict
comparison with the desired filled volume to be proved.
