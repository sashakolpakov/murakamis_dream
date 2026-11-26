# Real filling powers and a uniform bound for the outer shared indices

Research proof, 4 November 2026. Frozen manuscripts are unchanged.

The angle bound for a positive internal pair was previously proved
only at integer powers. This matters when comparing two actions by
differentiating with respect to a filling power. We first fill that
gap for the geometric problem. We then use the actual physical
normal-defect estimate to bound the outer shared indices in the
finite quantum sum. The estimate holds for every fixed positive
integer pair of powers at least three, through both level parities.

The two outside endpoints remain complete throughout. Nothing here
asserts a nonzero coefficient for the remaining middle integral.

## 1. The continuous geometric family

Give two adjacent selected vertices real powers \(n,p\ge3\), unit
charges, and one complete outside endpoint at each vertex. The
[real-power variational theorem](research_radical_path_sector_gap.md#6-a-uniform-estimate-for-every-positive-pair-of-powers-at-least-three)
gives the unique positive interior solution. Its angles depend
smoothly on the powers: the minimum is interior and its constrained
Hessian is positive definite. Write one angle as \(t=a-iH\).
The selected branches have \(0<a<\pi\), \(H>0\), and the original
period equation is
\[
 nt+2i\{r_0(t)+r_1(t,u)\}=2\pi,
 \quad r_0(t)=\operatorname{asinh}\tan(t/2),\quad
 r_1(t,u)=\operatorname{asinh}\{\tan(t/2)\cos(u/2)\}.
 \tag{1}
\]
Each return has positive real part and imaginary part between
\(-\pi/2\) and \(\pi/2\). The equation is logarithmic, with its
branch fixed by the positive geometry.

**Theorem 1.** For every real \(n,p\ge3\), both selected angles obey
\[
                  0<a<\pi/2,\qquad 0<H<107/100.
 \tag{2}
\]

We prove this by excluding a first angle with real part \(\pi/2\).
The starting pair \((3,3)\) has the strict angle bound by the
[integer-pair theorem](research_internal_pair_angle_bound.md).
Join it to any prescribed real pair by a straight segment of powers.
The positive solution exists along the whole segment. At a proposed
first boundary point, both real angles are at most \(\pi/2\).

Two elementary estimates supply a height bound at that boundary
without assuming the angle theorem that we are proving.

First, the cosine maximum principle holds for real powers. If an
active vertex maximized \(C=|\cos(t/2)|\ge1\), every neighbor would
have cosine modulus at most \(C\), including its complete neighbor.
Every incident return would then satisfy
\[
 \Re r\le\operatorname{asinh}|\sin(t/2)|
 \le\operatorname{asinh}\{\sqrt2\sinh(H/2)\}<3H/4.
 \tag{3}
\]
Here \(C\ge1\) implies \(|\sin(t/2)|^2\le2\sinh^2(H/2)\).
The last inequality follows from
\(\sinh(3H/4)>(3/2)\sinh(H/2)>\sqrt2\sinh(H/2)\).
The sum of at most two returns would be less than \(3H/2\),
contrary to its required value \(nH/2\). Thus both active cosine
moduli are strictly less than one. This argument uses no integrality.

Second, as long as \(a\le\pi/2\),
\(|\tan(t/2)|\le1\). The internal return has real part less than
\(\operatorname{asinh}1\), and the complete return increases with
\(a\) at fixed height. Its value at \(a=\pi/2\) is
\[
 k_0(H)=\operatorname{asinh}\sqrt{\operatorname{sech}H}.
\]
Consequently
\[
                    3H/2<k_0(H)+\operatorname{asinh}1.
 \tag{4}
\]
The right side decreases with \(H\). The exact Taylor comparisons
in [Proposition 1 of the complete-edge note](research_internal_pair_complete_edge_gap.md#1-the-height-bound-uses-the-actual-two-incidences)
give, at \(H=107/100\),
\[
 k_0(H)<18/25,\qquad \operatorname{asinh}1<441/500,
 \qquad 18/25+441/500<3H/2.
\]
Thus \(H<107/100<23/20\) at the proposed first boundary.

## 2. A first-quadrant barrier for continuous powers

At \(a=\pi/2\), put
\[
 \begin{split}
 \omega(H)&=\arctan(\sinh H),&
 \beta(H)&=\arctan\{\sqrt2\sinh(H/2)\},\\
 k_q(H)&=qH/2-k_0(H),&
 g_q(H)&=q\pi/4-\pi+\beta(H),&
 C_q(H)&=e^{i\omega}\sinh(k_q+ig_q).
 \end{split}
 \tag{5}
\]
The comparison power \(q\) is real. At the actual boundary
\(q=n\), the complete return is \(k_0-i\beta\), so the internal
return is exactly \(k_n+ig_n\). The other vertex still has real
angle at most \(\pi/2\). Consequently
\[
 C_n=\cos(u/2)\ \hbox{lies in the first quadrant},\qquad
                         \Re C_n^2\ge1/2.
 \tag{6}
\]
Here and below, \(\Re C^2\) means the real part of the complex
square, not the square of its real part.

The exact identity is
\[
 \Re C_q^2=\frac12\left[
 \cos(2\omega)\{\cosh(2k_q)\cos(2g_q)-1\}
 -\sin(2\omega)\sinh(2k_q)\sin(2g_q)\right].
 \tag{7}
\]
The coefficients of the two trigonometric terms differ. In
particular, they cannot be combined into
\(\cosh(2k_q)\cos(2g_q+2\omega)\).

**Lemma 2.** Fix \(0<H<23/20\). Along any first-quadrant part
of the curve \(q\mapsto C_q(H)\) with \(k_q>0\) and
\(-\pi/2<g_q<\pi/2\), an intersection with
\(\Re C_q^2=1/2\) has strictly negative derivative:
\[
                \left.\frac{d}{dq}\Re C_q^2\right|_{\Re C_q^2=1/2}<0.
 \tag{8}
\]

*Proof.* Write \(k=k_q\), \(g=g_q\), and
\(E=e^{i\omega}\cosh(k+ig)\). In the first quadrant, \(k>0\),
\(-\pi/2<g<\pi/2\), and
\[
 E=\tanh k\,C+\frac{e^{i\omega}\cos g}{\cosh k}
       \quad\hbox{also lies in the first quadrant},\qquad
 E^2=C^2+e^{2i\omega}.
 \tag{9}
\]
Direct differentiation gives
\[
 \frac{d}{dq}\Re C^2
       =\Re\{(H+i\pi/2)CE\}.
 \tag{10}
\]
At \(\Re C^2=1/2\), write \(C^2=1/2+iY\), \(Y>0\).
If \(1/2+\cos(2\omega)\le0\), then \(\arg E\ge\pi/4\).
Since \(H<\pi/2\), (10) is strictly negative.

Otherwise the real part of \(E^2\) is positive, and
\[
 \arg(CE)\ge\frac12\arg\{1/2+e^{2i\omega}\}
                         >\arctan(2H/\pi).
\]
For the last strict inequality it is enough, after substituting
\(\tan\omega=\sinh H\), to prove
\[
 \sinh H\,(\pi^2-4H^2)>H\pi(3-\sinh^2H).
 \tag{11}
\]
The factor \(\pi^2-4H^2\) is positive. The elementary lower bounds
\(\sinh H/H>1+H^2/6\) and
\(\sinh^2H>H^2+H^4/3\) show that the left side of (11), divided
by \(H\), minus its right side divided by \(H\), is greater than
\[
 \pi(\pi-3)+(\pi^2/6+\pi-4)H^2
                         +(\pi-2)H^4/3>0.
\]
All three coefficients are positive because \(\pi>3\).
This proves (11), hence (8). The argument also applies to the
positive real boundary of the quadrant, where \(Y=0\).
\(\square\)

There is at most one relevant first-quadrant interval in \(q\).
Indeed, for \(k\ge0\) and \(-\pi/2<g<\pi/2\), membership is
equivalent to
\[
 -\arctan(\sinh H\tanh k)<g
                      <\arctan(\tanh k/\sinh H).
 \tag{12}
\]
Along increasing \(q\), the lower boundary decreases while
\(g\) increases at rate \(\pi/4\). The upper boundary increases
at rate at most \(H/(2\sinh H)<1/2<\pi/4\). Thus the curve
cannot leave this quadrant and subsequently return before the
actual point in (6). The range of \(g\) between any of the
starting points below and the actual point is contained in
\((-\pi/2,\pi/2)\).

It remains to prove that this interval starts with
\(\Re C^2<1/2\). Put
\[
                    H_c=\frac23\operatorname{asinh}\sqrt2<\frac45.
 \tag{13}
\]
The [exact power-three calculation](research_internal_pair_angle_bound.md#3-a-vertex-of-power-three-cannot-reach-the-boundary)
gives
\[
 \begin{split}
 C_3(H)&=2\sinh H-\frac{\cosh(3H/2)}{\sqrt2}
              +i\left\{\frac{\sinh(3H/2)}{\sqrt2}-1\right\},\\
 \frac12-\Re C_3(H)^2
   &=4X^5-4X^4+8X^3-8X^2+X+1>0,\qquad
                    X=\sqrt2\sinh(H/2)<1.
 \end{split}
 \tag{14}
\]
The polynomial identity is unchanged by the correction in (7);
its two rational Bernstein tables prove positivity on \([0,1]\).

For \(H\ge H_c\), one has \(k_3>0\), \(-\pi/4<g_3<0\),
and \(\Im C_3\ge0\). Its real part is positive directly from
\(C_3=e^{i\omega}\sinh(k_3+ig_3)\).
Thus the curve starts, at \(q=3\), in the first quadrant or on
its positive real boundary, with \(\Re C_3^2<1/2\).
Lemma 2 and (12) prohibit a later upward crossing to (6).

For \(H<H_c\), consider the entry on the positive real axis.
Its nonnegative return \(k=k_{\rm ent}(H)\), when it exists,
satisfies
\[
 k=2H-\frac{2H}{\pi}
       \{\beta(H)+\arctan(\sinh H\tanh k)\}-k_0(H).
 \tag{15}
\]
The right side strictly decreases with \(k\). If it is negative
at \(k=0\), then at the first feasible value \(k_q=0\) one has
\(g_q>0\); the upper inequality in (12) already fails and
continues to fail. Such an \(H\) has no actual point (6).
Otherwise there is one nonnegative entry root.

This root increases with \(H\) while \(H\le H_c\). Here are
explicit bounds for the differentiation, to keep this assertion
independent of a numerical graph. For \(H\le4/5\),
\[
 \begin{gathered}
 \cosh H<7/5,\quad k_0(H)>3/4,\quad
 k_{\rm ent}<17/20,\quad \beta'(H)<3/4,\\
 \beta(H)+\omega(H)<\pi/2,\qquad \pi>25/8.
 \end{gathered}
 \tag{16}
\]
The bound for \(k_0\) follows from
\((7/5)(24/29)^2<1\) and \(\sinh(3/4)\le24/29\).
The bound for the entry follows immediately from (15).
Also
\(\beta'=\cosh(H/2)/(\sqrt2\cosh H)<3/4\).
For the angle sum use
\[
 \sinh H\,\sqrt2\sinh(H/2)
      <(60/67)(3/2)(30/73)<1,
\]
where the two hyperbolic-sine bounds are geometric majorants
of their positive Taylor series. At a fixed \(k\le17/20\),
the partial derivative in \(H\) of the right side of (15) is
therefore greater than
\[
 1-\frac{64}{125}\left\{\frac34+\frac75\frac{17}{20}\right\}
                       =\frac{21}{3125}>0.
 \tag{17}
\]
In deriving this bound the term \(-k_0'(H)\) is positive and
may be dropped. The implicit derivative is positive since the
right side of (15) decreases with \(k\). Its value at \(k=0\)
also increases with \(H\), so the entry roots form one interval,
ending at \(H_c\), rather than separate branches.

At the positive real entry,
\[
 \Re C_{\rm ent}^2=
 \frac{\sinh^2 k_{\rm ent}\cosh^2 k_{\rm ent}}
                       {\sinh^2 k_{\rm ent}+\operatorname{sech}^2H}.
 \tag{18}
\]
This expression increases with both \(k_{\rm ent}\) and \(H\).
At \(H=H_c\) the entry is exactly \(C_3(H_c)\), whose square
is less than \(1/2\) by (14). Hence every earlier nonnegative
entry has square less than \(1/2\). Lemma 2 again prohibits an
upward crossing to (6).

Both height ranges exclude the proposed first angle boundary.
The argument in (4) then supplies the height bound throughout
the real-power family. This proves Theorem 1.

## 3. Comparing the pair action with the two half-charge actions

Let \(\mathcal M(n,p)\) be the original stationary action's real
part for this complete-ended pair. Let \(\mu(n)\) be the real
half-charge action of the complete leaf, denoted \(M_n\) in the
[observation theorem](research_complete_source_pick_observation.md#5-a-nonzero-half-charge-observation).
Its angle is \(t_0=a_0-iH_0\), and
\[
 nt_0+2i\operatorname{asinh}\tan(t_0/2)=\pi,
 \qquad
 \mu(n)=\Re\{\Psi(t_0)+int_0^2/(4\pi)-it_0/2\}.
 \tag{19}
\]
Here \(\Psi(t)=\psi(t,0)\) has its original constant
\(\Psi(0)=M_\infty=4G/\pi\), where \(G\) is Catalan's constant.

The proof of the
[pair-to-half-charge position comparison](research_pair_half_charge_action_gap.md)
uses only the positive returns, \(n\ge3\), and the rectangle (2).
Theorem 1 has now established those hypotheses for real powers.
Thus at the vertex of power \(n\),
\[
                         a>a_0>0,\qquad H>H_0>0.
 \tag{20}
\]
In particular this extension does not differentiate through an
interval on which the original integer angle proof was unavailable.

At a stationary point all derivatives in the geometric variables
vanish. Differentiating the explicit filling term \(int^2/(4\pi)\)
therefore gives
\[
 \partial_n\mathcal M(n,p)=\frac{aH}{2\pi},\qquad
                       \mu'(n)=\frac{a_0H_0}{2\pi}.
 \tag{21}
\]
The same formula holds at the other vertex. These are derivatives
of the calibrated stationary actions, with no additive constant
changed as the powers vary. Consequently
\[
 \mathcal G(n,p):=\mathcal M(n,p)-\mu(n)-\mu(p)
 \quad\hbox{is strictly increasing in each real power},
 \qquad \mathcal G(n,p)\ge\mathcal G(3,3).
 \tag{22}
\]

We need a rational lower bound for this difference. The previously
certified geometric half-action gives
\(\mathcal M(3,3)>63/25\); see
[the triangular-normal comparison](research_pair_triangular_normal_region.md#3-the-two-first-normal-factors-are-below-the-geometric-rate).
The half-charge action admits the following upper bound without a
numerical integration.

On its power-three charge path \(0\le\chi\le1/2\), one has
\(a<\pi/3\), \(H<2/5\). Throughout that rectangle,
\[
             \frac{49}{50}<\Re\sec((a-iH)/2)<\frac76.
 \tag{23}
\]
For the lower bound use \(\Re\sec\ge\operatorname{sech}(H/2)\)
and \(\cosh(1/5)\le305/299<50/49\). For the upper bound use
\(\Re\sec\le\sec(a/2)\le2/\sqrt3<7/6\).
Integrating \(r_0'(t)=\sec(t/2)/2\) along horizontal and
vertical segments gives
\[
 k\ge49a/100,\qquad |g|\le7H/12.
\]
The two period equations \(k=3H/2\) and
\(3a+2|g|=2\pi\chi\) imply
\[
 H\ge\frac{588\pi}{3043}\chi,\qquad
 \mu(3)=M_\infty-\int_0^{1/2}H(\chi)\,d\chi
       \le M_\infty-\frac{147\pi}{6086}<\frac{219}{200}.
 \tag{24}
\]
The last comparison uses the proved rational estimate
\(M_\infty<7/6\), \(\pi>3\), and
\(7/6-441/6086=9989/9129<219/200\).
Combining (22) and (24) yields the uniform classical comparison
\[
            \boxed{\quad\mathcal G(n,p)>33/100
                         \qquad(n,p\ge3).\quad}
 \tag{25}
\]

## 4. The original low coefficients and the discarded indices

We now return to fixed integer powers \(n,p\ge3\).
At level \(N\), put \(L=\lfloor(N-1)/2\rfloor\), and retain
the literal low complete-end polynomial
\(\mathcal L_N(w)=\sum_{j=0}^{L}e_j(w)e_j(-2)\).
For odd levels this already equals the full complete-end kernel.
Define the actual traced coefficients
\[
 W_{n,j,N}=\phi_N[R^n\mathcal L_Ne_j],\qquad 0\le j\le L.
 \tag{26}
\]
All first normals are included in \(\phi_N\).
The [uniform physical-defect packet](research_physical_normal_defect_packet.md)
gives \(|D_{n,N}(c_a)|\le CN^A e^{N\mu(n)}\) at every
physical row, through both parities. Its rational leading
coefficient has no singularity on the physical interval.

Apply the exact normal-defect trace formula to (26).
All its node weights have polynomial size in \(N\), and
\[
 0\le e_j(c_a)\le e_j(-2)\quad(a\ge j),\qquad
                    e_j(c_a)=0\quad(a<j).
\]
The uniform sine-factorial bound gives
\[
 e_j(-2)\le CN^A e^{NV_0(j/N)},\qquad
 V_0(x)=-2J(1/2-x)-2J(x),\quad
 J(x)=\int_0^x\log(2\sin\pi s)\,ds.
 \tag{27}
\]
Thus, uniformly over every retained low index,
\[
                 |W_{n,j,N}|\le CN^A
                    e^{N\{\mu(n)+V_0(j/N)\}}.
 \tag{28}
\]
At odd levels the top index \(j=L\) has no contour term.
Its separate exact rank-one term has the half-charge packet
proved in [the odd observation note](research_odd_half_charge_observation.md#3-the-original-odd-trace-still-has-its-top-degree-term).
That packet also satisfies (28). No simple endpoint has been
assigned a nonexistent first normal.

The profile \(V_0\) is symmetric about \(1/4\), increases up
to that point, and decreases afterwards. At \(\beta=12/25\),
with \(\delta=1/2-\beta=1/50\),
\[
 \begin{split}
 V_0(\beta)
 &=-2\int_0^\delta\log\tan(\pi s)\,ds\\
 &\le\frac1{25}\{1+\log(50/\pi)\}<\frac{31}{200}.
 \end{split}
 \tag{29}
\]
Here \(\tan(\pi s)\ge\pi s\). The last strict comparison
uses \(\pi>3\) and \(e^{23/8}>50/3\); the latter already
follows from the first seven positive exponential Taylor terms.
The same bound holds when \(x\le1/50\) or \(x\ge12/25\).

**Theorem 3.** For every fixed integer \(n,p\ge3\), define
\[
 \mathcal T_N=\{0\le j\le L:j/N\le1/50
                                  \ \hbox{or}\ j/N\ge12/25\}.
\]
There are constants \(C,A\), depending on the fixed powers,
such that at both parities
\[
 \boxed{\quad
 \sum_{j\in\mathcal T_N}|W_{n,j,N}W_{p,j,N}|
       \le CN^A e^{N\{\mathcal M(n,p)-1/50\}}.
 \quad}
 \tag{30}
\]

*Proof.* There are at most \(N\) terms. Equations (28)–(29)
give the rate \(\mu(n)+\mu(p)+31/100\). By (25) this is
strictly less than \(\mathcal M(n,p)-1/50\). Absorb the
number of terms and all fixed finite levels in the polynomial
factor. The argument bounds the sum of absolute values, so no
unproved cancellation between the discarded indices is used.
\(\square\)

The theorem is a bound after taking the two original traces.
It does not give the same bound for a bare internal kernel on
a fixed complex-angle contour. In particular it does not
remove the endpoint obstruction to a full bare-kernel packet.

The previously proved radical-sector estimates also permit
replacement of the three full edge kernels by their low parts
in the complete-ended pair: that error has rate at most
\(2M_\infty<7/3\), whereas
\(\mathcal M(n,p)\ge\mathcal M(3,3)>63/25\).
Together with (30), this reduces the full original pair to the
retained range
\[
                            1/50<j/N<12/25
 \tag{31}
\]
with an error below \(\mathcal M(n,p)-1/50\).
The remaining joint cycle over this middle range still has to be
controlled. The estimate neither replaces that cycle by a single
bare edge saddle nor proves its global noncancellation.

## 5. Uniform geometry when both powers are at least seven

The real period equation does not permit assuming that every
imaginary return is negative. In particular the internal return
at one vertex can have positive imaginary part when its neighbor
has a different power. The following bootstrap allows that sign
and gives bounds uniform over all real \(n,p\ge7\).

**Theorem 4.** In the complete-ended unit-charge pair of Section 1,
if \(n,p\ge7\), then both selected angles \(t_i=a_i-iH_i\)
and the original internal wire \(x=\xi+iY\) satisfy
\[
 0<a_i<\frac{19}{20},\qquad
 0<H_i<\frac3{10},\qquad
                         0<2\pi Y<\frac14.
 \tag{32}
\]

*Proof.* The proved pair angle bound gives \(a_i<\pi/2\).
The cosine maximum principle gives \(|\cos(t_i/2)|<1\);
its proof uses only positive real returns, degree two, and real
powers at least three, so it applies to the real-power family here.
Consequently \(|\tan(t_i/2)|<1\), and each of the two original
return arguments at a vertex has modulus less than one.
From their imaginary period equation,
\[
 \frac{nH}{2}=\Re r_0+\Re r_1<2\operatorname{asinh}1,
 \qquad H<\frac{4\operatorname{asinh}1}{7}<\frac{18}{35}.
 \tag{33}
\]
The last inequality uses \(\operatorname{asinh}1<9/10\),
which follows from the first three positive terms of
\(\sinh(9/10)\).

Write \(C=\cos(u/2)\) for the neighbor cosine.
Its real part is positive, and
\[
 0<\Im C<\frac57\sinh(9/35)<\frac15.
\]
Here \(\sin(a_u/2)<1/\sqrt2<5/7\).
Also \(\Im\tan(t/2)<0\) and
\(\Re\tan(t/2)\le\tan(a/2)\). Thus
\(\Im\{\tan(t/2)C\}\le\tan(a/2)/5<1/5\).
If \(r_1=k_1+ig_1\) has \(g_1>0\), then
\(\sin g_1=\Im(\tan(t/2)C)/\cosh k_1\).
For \(0\le z\le1/5\),
\(\arcsin z\le z/\sqrt{1-z^2}<(25/24)z\).
It follows, also when \(g_1\le0\), that
\(g_1\le(5/24)\tan(a/2)\).
The complete return has \(g_0<0\). The real period therefore
gives
\[
 \begin{split}
 na&=2\pi+2g_0+2g_1
      <2\pi+\frac5{12}\tan(a/2)
      \le2\pi+\frac5{6\pi}a
      <2\pi+\frac4{15}a,\\
 a&<\frac{2\pi}{n-4/15}
      \le\frac{30\pi}{101}<\frac{660}{707}<\frac{19}{20},
 \qquad \cos a>\frac{29}{50}.
 \end{split}
 \tag{34}
\]
The chord bound for the convex function \(\tan\) on
\([0,\pi/4]\) proves \(\tan(a/2)\le2a/\pi\).
We used \(25/8<\pi<22/7\); the alternating cosine series
through degree six at \(19/20\) proves the last lower bound.

Two short height improvements now suffice. Since
\(\cosh(18/35)<8/7\), equations (33)–(34) give
\[
 |\tan(t/2)|^2
 =\frac{\cosh H-\cos a}{\cosh H+\cos a}
 <\frac{8/7-29/50}{8/7+29/50}
 =\frac{197}{603}<\sinh^2(14/25).
 \tag{35}
\]
Both real returns are at most
\(\operatorname{asinh}|\tan(t/2)|\), because the neighbor
cosine has modulus less than one. Hence
\(H<(4/7)(14/25)=8/25\).
The estimate \(\cosh(8/25)<53/50\) then gives
\[
 |\tan(t/2)|^2
   <\frac{53/50-29/50}{53/50+29/50}
   =\frac{12}{41}<\sinh^2(21/40),
 \qquad H<\frac47\frac{21}{40}=\frac3{10}.
 \tag{36}
\]
The two sinh comparisons already follow from \(\sinh z>z+z^3/6\).
The cosh bounds follow from
\(\cosh z\le1+z^2/[2(1-z^2/12)]\).

For the wire, put \(A=\cos^2(t_n/2)\) and
\(B=\cos^2(t_p/2)\). The preceding estimates imply
\[
 \begin{split}
 |A-1|, |B-1|
 &<r:=\left(\frac{19}{40}\right)^2
       +\left(\frac{3/20}{1-(3/20)^2/6}\right)^2\\
 &=\frac{252350449}{1016334400}<\frac14.
 \end{split}
 \tag{37}
\]
Indeed \(|1-A|=|\sin(t_n/2)|^2
=\sin^2(a_n/2)+\sinh^2(H_n/2)\), and similarly for \(B\).
The positive sinh series is bounded by \(z/(1-z^2/6)\).

The disk \(D(1,r)\) is closed under the harmonic mean.
To see this, inversion maps it to the convex disk with center
\(1/(1-r^2)\) and radius \(r/(1-r^2)\). Averaging two
points in that disk and inverting again returns to \(D(1,r)\).
Thus the original wire parameter obeys
\[
 k=\frac{AB}{A+B}\in D(1/2,r/2),\qquad
 \cosh(2\pi Y)=|k|+|1-k|\le\sqrt{1+r^2},
 \qquad 2\pi Y\le\operatorname{asinh}r<\frac14.
 \tag{38}
\]
The focal-distance bound follows by Cauchy–Schwarz:
\(|k|^2+|1-k|^2=1/2+2|k-1/2|^2\le(1+r^2)/2\).
The selected wire branch has \(Y>0\), as proved by its original
geometric continuation. This proves (32). \(\square\)

**Corollary.** The selected internal wire also satisfies
\(1/5<\xi<1/4\).

*Proof.* The disk in (38) gives \(\Re k>3/8\). The original
wire order supplies \(0<\xi<1/4\), and therefore
\[
 0<\cos(2\pi\xi)\cosh(2\pi Y)=1-2\Re k<\frac14.
\]
It follows that
\(\cos(2\pi\xi)<1/4<\cos(2\pi/5)=(\sqrt5-1)/4\).
Strict decrease of the cosine on this interval proves the lower
bound. \(\square\)

The thresholds in the mixed-phase concavity theorem consequently
have a common fixed margin. For
\(\alpha(s)=\arccos(\operatorname{sech}(2\pi s))/(2\pi)\),
the identity \(\arccos(\operatorname{sech}z)=\arctan(\sinh z)\)
and its derivative \(\operatorname{sech}z<1\) give
\[
 \alpha(Y)<\frac1{8\pi}<\frac1{25},\qquad
 \alpha(H_i/(2\pi))<\frac3{20\pi}<\frac1{20}
                                                   <\frac3{50}.
 \tag{39}
\]
These are geometric domain bounds. They do not, by themselves,
estimate the contour connectors or prove a nonzero coefficient
in the finite source.

## 6. An original-action lower bound for powers at least seven

The action monotonicity also turns one rigorously enclosed positive
point into a uniform bound on a whole power quadrant. The calibration
here uses the original unexponentiated periods and all three edges.
It supplies a geometric comparison constant, not a new quantum
coefficient.

**Theorem 5.** For every real \(n,p\ge7\),
\[
                    \mathcal M(n,p)>\frac{163}{50}.
 \tag{40}
\]

*Proof.* At \(n=p=7\) the original equations are
\[
 \begin{split}
 7t+2i\{\operatorname{asinh}\tan(t/2)
       +\operatorname{asinh}(\tan(t/2)\cos(u/2))\}&=2\pi,\\
 7u+2i\{\operatorname{asinh}\tan(u/2)
       +\operatorname{asinh}(\tan(u/2)\cos(t/2))\}&=2\pi.
 \end{split}
 \tag{41}
\]
The [focused outward certificate](../experiments/certify_pair_seven_action.py)
first finds an approximate symmetric solution, then proves the
existence of a solution to (41) by a rectangular interval contraction
in both complex variables. The recorded box has radius \(2^{-100}\)
in each real coordinate. A fixed inverse of its central Jacobian
gives a self-map strictly inside the box, with complex maximum-norm
derivative bound less than \(8\cdot10^{-31}\).
This is an existence proof for the original logarithmic equations;
the numerical candidate is not used as an exact root.
The symmetric box and uniqueness also imply \(t=u\).

Every return argument lies in the right half-plane throughout the
box. On each of the original edges \((t,0),(t,u),(u,0)\), the checker
certifies the positive-domain inequality
\(\Re q>\sqrt{(\Re a)^2+(\Re b)^2}\), with margin greater
than \(1/2\), where \(a=\tan(t_{\rm left}/2)\),
\(b=\tan(t_{\rm right}/2)\), and \(q=\sqrt{1+a^2+b^2}\).
It also checks that the four distinct original shape expressions
have positive imaginary parts and that
\(\cosh r=q\cos(t_{\rm neighbor}/2)\) has the selected positive
real-part sign. Thus this root belongs to the original positive
variational domain and is the selected pair solution. Positivity
of the returns alone is not substituted for positivity of the
original edges.

For the action put
\[
 \begin{split}
 A&=\cos^2(t/2),\qquad B=\cos^2(u/2),\qquad
 x=\pi^{-1}\arctan\sqrt{\frac{AB}{A+B-AB}},\\
 J(z)&=\frac{\operatorname{Li}_2(1)
               -\operatorname{Li}_2(e^{2\pi iz})}{2\pi i}
                     +\frac{i\pi}{2}z(1-z),\\
 b(x,t)&=-J(1/2-x+t/(2\pi))-J(1/2-x-t/(2\pi))-2J(x),\\
 \Psi(t)&=-4J(1/4+t/(4\pi))-4J(1/4-t/(4\pi)),\\
 \mathcal S_{77}
   &=b(x,t)+b(x,u)+\Psi(t)+\Psi(u)
                     +\frac{7i(t^2+u^2)}{4\pi}-i(t+u).
 \end{split}
 \tag{42}
\]
The square root is in the first quadrant and the arctangent is
its selected continuation, giving \(1/5<\Re x<1/4\) and
\(\Im x>0\). Every argument of \(J\) stays in
\(0<\Re z<1\), where its displayed formula is holomorphic:
the exponential avoids the principal dilogarithm cut
\([1,\infty)\). Differentiating gives
\(J'(z)=\Log(2\sin\pi z)\) on the original strip, and its
limit at zero is zero. This fixes the constant and branch of
the [original mixed phase](research_mixed_wire_phase_concavity.md).
In particular \(\Psi(0)=M_\infty\); no additive real constant
is chosen at the certified point.

Outward complex-ball evaluation on the entire root box proves
\[
       3.2624704255<\Re\mathcal S_{77}<3.2624704256 .
 \tag{43}
\]
The checker additionally encloses the original wire and angular
gradient lifts and verifies their agreement with the selected
return branches. The root, branch inequalities, action enclosure,
and source hashes are in the
[saved certificate](../repro/results/research-pair-seven-action.json).
Thus \(\mathcal M(7,7)>163/50\).
Finally the already proved derivatives
\(\partial_n\mathcal M=aH/(2\pi)>0\) and
\(\partial_p\mathcal M=a'H'/(2\pi)>0\)
on the real positive pair family extend the bound to every
\(n,p\ge7\), proving (40). \(\square\)

Run the checker with:

~~~sh
python3 experiments/certify_pair_seven_action.py
~~~

It uses rigorous Arb balls for every successful comparison,
including the dilogarithms. The contour contraction and the
positive-domain identification above are the proof of the root's
status; no scan of numerical solutions or inferred quantum
asymptotic is used.

## 7. A global comparison for real trace angles

The preceding action bound is useful only when the other portions of
the finite sum can be compared with it. We now make that comparison
when at least one real trace angle is beyond its factorial wall.
The wire may already have its full geometric imaginary part.
The final conclusion is an upper bound on these portions of the
source, not a proof that they join to a complete admissible contour.

First, the same geometry gives a sharper wire-height estimate:
\[
                         L:=2\pi Y<\frac2{15}
                         \qquad(n,p\ge7).
 \tag{44}
\]
Here is a rational proof. Equation (34) gives
\(a<660/707<15/16\). The alternating sine and cosine series give
\(\sin a<81/100\) and \(\cos a>59/100\).
For \(A=\cos^2(t_n/2)\), and likewise for \(B=\cos^2(t_p/2)\),
the already proved \(H_i<3/10\) and \(|\cos(t_i/2)|<1\) imply
\[
 \ell:=\frac{159}{200}<\Re A,\Re B<1,\qquad
 0<\Im A,\Im B<b_0:=\frac{243}{1970}.
 \tag{45}
\]
Indeed \(\Re A=(1+\cos a\cosh H)/2\), while
\(\Im A=\sin a\sinh H/2\) and
\(\sinh(3/10)<60/197\).
For \(k=AB/(A+B)\), direct multiplication gives
\[
 \begin{split}
 \Im k
 &=\frac{\Im B\,|A|^2+\Im A\,|B|^2}{|A+B|^2}\\
 &<b_0\left\{\frac12+
          \frac{(1-\ell)^2+b_0^2}{8\ell^2}\right\}.
 \end{split}
 \tag{46}
\]
We used
\(|A|^2+|B|^2=(|A+B|^2+|A-B|^2)/2\),
\(|A-B|^2<(1-\ell)^2+b_0^2\), and
\(|A+B|^2>4\ell^2\).
The original identity \(k=\sin^2(\pi x_*)\) and
\(1/5<\Re x_*<1/4\) give
\[
 \sinh L
 =\frac{2\Im k}{\sin(2\pi\Re x_*)}
 <\frac{108361228815}{816082404766}<\frac2{15}.
 \tag{47}
\]
For the denominator use \(\sin(2\pi/5)>19/20\), which follows
from \(\sin^2(2\pi/5)=(5+\sqrt5)/8\) and
\(\sqrt5>111/50\). Since \(L<\sinh L\), this proves (44).

Let \(V_\tau(\xi)=\mathfrak b(\xi,\tau)\) be the real Newton
profile, with the continuous factorial upper exponent
\(\mathfrak b\) defined in
[the uniform factorial bound](research_uniform_factorial_and_boundary_decay.md#3-the-exact-newton-interpolation).
For real \(\tau\), its change with wire height satisfies
\[
 0\le \mathfrak b(\xi+iy,\tau)-V_\tau(\xi)
       \le\pi|y|,\qquad
          0<\xi<1/2,\quad |\tau|\le\pi.
 \tag{48}
\]
To prove this, first suppose \(y>0\) and \(|\tau|<\pi\).
Put \(z=\pi(\xi+iy)\). Differentiation in \(x\) uses the
individual continued logarithms
\[
 b_x=\Log\cos(z+\tau/2)+\Log\cos(z-\tau/2)-2\Log\sin z.
 \tag{49}
\]
Their exponential is
\(\cos^2(\tau/2)\csc^2z-1\), which lies strictly in the lower
half-plane: \(\Im(\sin^2z)>0\).
At \(\tau=0\), the imaginary part of (49) is
\(2\arg\cot z\in(-\pi,0)\). Varying the real angle keeps its
exponential in that same half-plane, so the continued logarithm
has imaginary part in \((-\pi,0)\) throughout. Therefore
\(0<\partial_y\mathfrak b<\pi\).
Integration from zero proves (48) for positive \(y\).
Conjugation gives negative \(y\), and continuity includes the
factorial wall and the angular endpoints. This proof fixes the
logarithmic lift before using the quotient; it does not reset
the branch at a reflected factorial argument.

For \(0<\xi<1/2\), define
\[
 \begin{split}
 C(\xi)&=J(2\xi)-2J(\xi)+\Psi(\pi-2\pi\xi),\\
 B(\xi)&=C(\xi)+V_0(\xi)+M_\infty.
 \end{split}
 \tag{50}
\]
If \(|\tau|\ge\pi-2\pi\xi\) and \(|\rho|\le\pi\), the
real-angle monotonicity of \(V_\tau\) and \(\Psi\) gives
\[
 V_\tau(\xi)+\Psi(\tau)+V_\rho(\xi)+\Psi(\rho)
                  \le B(\xi).
 \tag{51}
\]
The derivative of \(V_\tau\) is an integrable logarithm at its
wall; its sign remains negative on both sides. Thus this
comparison applies on the whole interval \(0<\xi<1/2\).

**Theorem 6.** The maximum in (51) has the bound
\[
 B(\xi)\le B(1/3)
       =M_\infty-18J(1/3)
       <\frac{57641}{18500}<\frac{25}{8}.
 \tag{52}
\]
Consequently, for every fixed integer pair \(n,p\ge7\), the
complete upper phase with real trace angles and \(|y|\le Y\)
satisfies
\[
 \mathcal E_{n,p}(\xi+iy,\tau,\rho)
 <\frac{391}{120}
 <\mathcal M(n,p)-\frac1{600}
 \tag{53}
\]
whenever at least one of the two angles is beyond its wall.
Here \(\mathcal E_{n,p}\) includes the original wire penalty
from equation (22) of
[the contour reduction](research_internal_pair_combined_contour_reduction.md#4-one-explicit-function-bounds-all-sixteen-pieces).

*Proof.* Differentiating (50), with
\(\Psi(\pi-2\pi\xi)=-4J((1-\xi)/2)-4J(\xi/2)\), gives
\[
 B'(\xi)=2\log\frac{2\cos^2(\pi\xi)}{1-\cos(\pi\xi)}.
 \tag{54}
\]
This derivative decreases strictly and vanishes only at
\(\xi=1/3\). Reflection and duplication of \(J\) give
\(J(2/3)=-J(1/3)\) and \(3J(1/3)=2J(1/6)\);
substitution in (50) yields the equality in (52).

For its rational bound, the absolutely convergent sine series gives
\[
 -J(1/3)=\frac{\sqrt3}{4\pi}
    \sum_{j\ge0}\left\{\frac1{(3j+1)^2}-\frac1{(3j+2)^2}\right\}.
 \tag{55}
\]
The summand decreases with \(j\). The terms starting at \(j=3\)
therefore sum to at most
\(21/12100+1/330<2/1000+1/300\).
The first three terms plus this latter bound equal
\(920357/1176000<157/200\).
Use \(M_\infty<7/6\), \(\sqrt3<26/15\), and
\(\pi>333/106\) to obtain
\[
 M_\infty-18J(1/3)
 <\frac76+\frac{18(26/15)}{4(333/106)}\,\frac{157}{200}
 =\frac{57641}{18500}<\frac{25}{8}.
 \tag{56}
\]
Finally apply (48) twice. The total wire correction is at most
\(2\pi|y|\le L<2/15\); the lower-wire penalty can only decrease
the exponent. The real crossing phases contribute zero at real
trace angles. Since
\(163/50-25/8-2/15=1/600\), (40) proves (53).
\(\square\)

For a fixed compact index interval \([\alpha,\beta]\subset(0,1/2)\)
and a fixed angular cut \(T<\pi\), (53) gives a finite-source
bound on sufficiently small positive trace heights, with gap
\(1/1200\). Here the reflected region is specified by the
real angles before those heights are introduced. Uniform
continuity includes its factorial walls. The complete kernels
have their proved low-kernel phase on the compact neighborhood,
and decreasing the heights further gives
\(\Re\Psi(t)>|\Im t|\), so their radicals have smaller rate.
At fixed nonzero wire heights, or on half-grid vertical sides,
the original wire denominator has its prescribed exponential
weight and a bounded remaining factor. The trace denominators
require positive heights. Thus the real-angle statement (53)
is not being applied directly to a singular trace contour.
The uniform factorial upper bound supplies the actual density
estimate at both parities, and smaller holomorphic neighborhoods
retain every fixed selected ordinary-color derivative.

## 8. Two useful endpoint cuts

The full geometric wire rectangle can be used at the left cut.
For \(0<\xi\le3/50\), \(|y|\le Y\), and real trace angles,
the real-angle monotonicity gives
\(\mathfrak b(\xi+iy,\tau)\le\Re b(\xi+iy,0)\).
The function \(\Re b(\xi+iy,0)\) increases with \(\xi<1/4\):
its derivative is \(2\log|\cot(\pi(\xi+iy))|>0\).
Equation (48), applied at zero angle, therefore implies
\[
 \mathfrak b(\xi+iy,\tau)
       \le V_0(3/50)+\pi|y|,\qquad
 V_0(3/50)<\frac{33}{100}.
 \tag{57}
\]
For the last inequality integrate
\(V_0'(x)=2\log\cot(\pi x)\le2\log(1/(\pi x))\)
from zero. Use \(\pi>3\) and
\(\log(50/9)<7/4\); the latter follows already from
\(\sum_{k=0}^4(7/4)^k/k!=34193/6144>50/9\).
The two factors and the complete phases have total rate
\[
 2V_0(3/50)+2M_\infty+2\pi Y
 <\frac{33}{50}+\frac73+\frac14
 =\frac{973}{300}
 <\mathcal M(n,p)-\frac1{60}.
 \tag{58}
\]
We have used the earlier \(2\pi Y<1/4\), which already suffices.
As above, small positive trace heights preserve half the gap
on any compact left interval \([\alpha,3/50]\).
This includes half-grid vertical wire sides with \(|y|\le Y\).
It retains the full complete kernels, both level parities, and
fixed selected ordinary derivatives.

There is a different estimate for the right endpoint, after
the two original traces have been taken. In the notation (26),
the half-charge action satisfies \(\mu(n)<M_\infty\).
Equations (27)–(28) and the symmetry of \(V_0\) show
\[
 V_0(j/N)\le V_0(1/10)<\frac9{20}
                \quad\text{when }2/5\le j/N\le1/2.
 \tag{59}
\]
Indeed \(V_0(1/10)\le[1+\log(10/\pi)]/5\);
\(\pi>3\) and
\(\sum_{k=0}^4(5/4)^k/k!=7083/2048>10/3\)
give the strict bound.
Consequently
\[
 \sum_{2/5\le j/N\le L/N}|W_{n,j,N}W_{p,j,N}|
 \le CN^A e^{97N/30}
 <CN^A e^{N\{\mathcal M(n,p)-2/75\}} .
 \tag{60}
\]
The index \(L=\lfloor(N-1)/2\rfloor\) here is the one in
Section 4, not the height notation used in Section 7.
The odd simple endpoint is already included in (28).
Replacing full edge kernels by their low parts has rate at
most \(2M_\infty<7/3\), so it is smaller than the bound in
(60). These facts justify choosing the right index cut at
\(2/5+O(N^{-1})\) in the original source, with any slightly
smaller gap if rounding is needed. This is an estimate after
the traces; it does not assert the same bound on every
vertical segment in a complex wire deformation.

## 9. Reproduction and proof scope

The [exact scalar checker](../experiments/check_real_pair_geometry_and_tail_gap.py)
verifies the rational comparisons used above and reads the saved
\((3,3)\) action enclosure. It does not infer the geometric
continuation, monotonicity, or quantum bound from samples; those
arguments are the written proofs in Sections 1–5.

~~~sh
python3 experiments/check_real_pair_geometry_and_tail_gap.py
~~~

The [saved record](../repro/results/research-real-pair-geometry-and-tail-gap.json)
records the exact comparisons and the proof/input hashes.

An earlier draft used the false identity
\[
 \Re\bigl[\{e^{i\omega}\sinh(k+ig)\}^2\bigr]
 =\tfrac12\{\cosh(2k)\cos(2g+2\omega)-\cos(2\omega)\}.
\]
The missing distinction between the \(\cosh(2k)\) and
\(\sinh(2k)\) coefficients invalidated its asserted global
derivative sign. Equation (7) is the corrected identity.
The present proof instead uses a downward crossing at
\(\Re C^2=1/2\) and an explicit bound at the quadrant entry;
it makes no claim that the comparison is globally decreasing.
The corresponding integer-angle argument was also repaired.
The corrected geometric and finite-source implications have
been independently checked. This correction changes the written
proof; it does not replace a source estimate by a scalar test.

The final scalar replay refreshes the proof/input hashes after
those written corrections. No frozen pair-height certificate
input is changed by this note.
