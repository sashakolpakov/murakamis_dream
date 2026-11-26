# Optimizing the real variables during a boundary-height reset

Research deduction, 5 November 2026. A height comparison for a
selected boundary coordinate must pay the response of all free real
indices, not only the second derivative at fixed indices. This note
proves an upper bound for that response, including constrained
maximizers and changes of active faces. It gives a precise matrix
target for the first selected type-four coordinate. Its uniform
matrix inequality and the other Fourier branch are not assumed to
have been proved. No numerical computation is used.

## 1. A fixed horizontal domain

Let \(K\subset\mathbb R^d\) be a nonempty compact convex set,
and let \(I\) be a compact real interval. Fix a coordinate vector
\(v\) of length one and a reference height vector \(h_0\).
Suppose \(\Phi\) is holomorphic on a neighborhood of
\[
 \{x+i h_0+i(k-k_0)v:x\in K,\ k\in I\}.
 \tag{1}
\]
Subtract any fixed real affine function \(\ell(x)\) and put
\[
 f(x,k)=\Re\Phi(x+i h_0+i(k-k_0)v)-\ell(x),\qquad
 G(k)=\max_{x\in K}f(x,k).
 \tag{2}
\]
All derivatives below are evaluated at the indicated complex point.
Write
\[
 A=-\Re\Phi'',\qquad C=-\Im\Phi'',\qquad
 A\succeq\mu I_d\quad\text{on (1)},\qquad\mu>0.
 \tag{3}
\]
The affine subtraction does not change these matrices. In particular
\(f\) is uniformly strictly concave in its real variables, so
its maximizer \(x(k)\in K\) exists and is unique. It need
not be an interior point of \(K\).

**Lemma 1.** The map \(x:I\to K\) is Lipschitz. The value
\(G\) is continuously differentiable with Lipschitz derivative,
with one-sided derivatives at interval endpoints, and
\[
 G'(k)=f_k(x(k),k).
 \tag{4}
\]
For almost every interior \(k\),
\[
 v^TAv\ \le\ G''(k)\ \le\
 v^TAv+(Cv)^TA^{-1}(Cv),
 \tag{5}
\]
where the matrices on the right are evaluated at \(x(k),k\).
The upper bound remains valid through changes of the optimizer's
active faces; no differentiable choice of a fixed active set is
required.

*Proof.* Put \(p=f_x\). The variational inequalities for two
maximizers \(x=x(k)\), \(x_t=x(k+t)\) give
\[
 p(x,k)\cdot(x_t-x)\le0,
 \quad p(x_t,k+t)\cdot(x_t-x)\ge0.
 \tag{6}
\]
At fixed height, (3) makes \(p\) strongly decreasing. Also
\(f_{xk}\) is bounded, say by \(L\), on the compact set.
Subtracting (6) therefore yields
\(\mu\|x_t-x\|^2\le L|t|\|x_t-x\|\).
Thus \(\|x_t-x\|\le L|t|/\mu\).

For the derivative of the value, use the two trial points \(x\)
and \(x_t\):
\[
 f(x,k+t)-f(x,k)\le G(k+t)-G(k)
 \le f(x_t,k+t)-f(x_t,k).
 \tag{7}
\]
Both divided differences tend to \(f_k(x,k)\), using
continuity of \(x(k)\). For negative \(t\) the divided
inequalities reverse, with the same limit. This proves (4).
Since \(x\) is Lipschitz and \(f_k\) has bounded first
derivatives, \(G'\) is Lipschitz as well.

Almost everywhere, \(x'\) and \(G''\) exist. Holomorphy
gives the exact real identities
\[
 f_{xx}=-A,\qquad f_{xk}=Cv=:q,\qquad f_{kk}=v^TAv.
 \tag{8}
\]
Expand the difference of (6), divide by \(t^2\), and let
\(t\to0\) at such a differentiability point. The result is
\[
             x'^TAx'\le q^Tx'.
 \tag{9}
\]
Let \(r=q^TA^{-1}q\). Cauchy--Schwarz in the positive
\(A\)-metric implies
\((q^Tx')^2\le r\,x'^TAx'\le r\,q^Tx'\).
Equation (9) first shows \(q^Tx'\ge0\), and these
inequalities then give \(0\le q^Tx'\le r\), including
the case \(q^Tx'=0\). Differentiating (4) almost everywhere
now gives \(G''=v^TAv+q^Tx'\), proving (5).

This proof uses only the fixed convex set and its variational
inequalities. In the unconstrained case (9) is an equality with
\(x'=A^{-1}q\), so the upper expression in (5) is exact.
At a constrained point the response can be smaller. \(\square\)

## 2. An integrated budget at the original reference

Assume that \(x_0\in K\) is the original critical real
point at height \(c\), after subtracting the prescribed cut
tangent, and that the original first-height marginal also vanishes:
\[
 f_x(x_0,c)=0,\qquad f_k(x_0,c)=0.
 \tag{10}
\]
Strict concavity gives \(x(c)=x_0\), even if one allows a
closed box having \(x_0\) on its boundary. In particular
\(G(c)=f(x_0,c)\) and \(G'(c)=0\).
If
\[
 v^TAv+(Cv)^TA^{-1}(Cv)\le K_0
                  \quad(c\le k\le H)
 \tag{11}
\]
on every optimizing point, it follows from the absolute continuity
of \(G'\) that
\[
 G(H)-G(c)=\int_c^H(H-k)G''(k)\,dk
                    \le\frac{K_0}{2}(H-c)^2.
 \tag{12}
\]
Checking (11) on the whole box is sufficient. A proved optimizer
enclosure would also suffice. Neither version requires the maximizer
to remain in the interior or on one fixed face.

For the first type-four coordinate, take \(v\) to be the
first retained coordinate's height direction and take the original
joint cap-plus-incidence phase (13) of
[the height-tangent note](research_mixed_first_cap_height_tangent.md).
The variables include the cap's private coordinate, the next
conditional index, the first real coordinate and, when it is varied,
the outgoing cut coordinate. Subtract the original cut tangent
\(\Re[p_b(b-b_*)]\), where
\(p_b=\mathcal F_b\) at the actual reference. The original
private equations and the zero-lift equation
\((1-EU)(1-SU)=S(1-U)^3\) give (10); the zero lift is
essential for its second equality.

**Conditional factorial-branch consequence.** If this fixed-domain
comparison satisfies (3), (11) with \(K_0\le6\pi\), and
the actual first height satisfies \(c\ge-39/500=-.078\),
then at the selected height \(H=7/500\),
\[
 \begin{split}
 \max_{x\in K}\{f(x,H)-2\pi H\}
 &\le G(c)-\frac{163\pi}{62500}\\
 &<G(c)-\frac1{200}.
 \end{split}
 \tag{13}
\]
Indeed \(H-c\le23/250\), so the difference is bounded by
\(3\pi(23/250)^2-2\pi(7/500)
=-163\pi/62500\); \(\pi>3\) gives the last inequality.
This is a conditional matrix budget, not a verified uniform bound
on the original current product. In particular (11) is not supplied
by a lower bound for \(A\), nor by a bound for \(A_{zz}\)
alone. The stated height premise is likewise explicit here; no
unreviewed image extraction is imported.

## 3. The forced branch is a distinct optimization

The other actual Fourier rate is
\(\Re\mathcal F+\Re g(z)\), rather than
\(\Re\mathcal F-2\pi H\). Its target Hessian and height
response are those of \(\widetilde\Phi=\Phi+g(z)\):
\[
 \widetilde A=A-\Re g''(z)vv^T,
 \qquad \widetilde C=C-\Im g''(z)vv^T.
 \tag{14}
\]
Lemma 1 applies if this modified phase is uniformly horizontally
concave on the fixed domain. But its maximizing point at \(c\)
need not be the original reference, since the added \(g\) changes
its real gradient. Its initial value and initial height derivative
must therefore be paid separately, or it must be compared directly
by another valid support bound. Equation (13) alone does not control
the complete selected Fourier polynomial.

Even after both branch maxima have been bounded, the remaining
private real tails, conditional real tails, connecting currents and
aliases must still be included. The lemma only provides the correct
optimization rule for a phase on a fixed regular horizontal domain.

## 4. A proved fixed-index intermediate for a four-four prefix

Here is a genuine reset bound which illustrates the distinction.
It uses only the previously proved actual rectangles, without the
stronger height premise in (13). Let \(m\ge3\), let the first
two types be four, and keep \(e=e_*\), \(s=s_*\), and
\(b=b_*\) at their original critical values. Write
\(z_*=a+ic\). The
[endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md),
[ordinary height bounds](research_mixed_cyclic_critical_height_bounds.md)
and [shared-wire extraction](research_mixed_reduced_disk_pair_sums.md)
give
\[
 \begin{gathered}
 .246<a<.350,\quad -.108<c<-.020,\quad
 .333<\Re e_*<.363,\quad\Im e_*<0,\quad\Im s_*<0,\\
 .23<\Re s_*<.45,\qquad
 \Re(e_*+z_*)>1/2,\quad .545<\Re(s_*+z_*)<.77.
 \end{gathered}
 \tag{15}
\]
At length three the second ordinary block's external inputs may
both be attached; the shared-wire theorem still applies. Set
\(f_*(k)=\Re\mathcal F(e_*,s_*;a+ik,b_*)\).
Its original zero marginal gives \(f_*'(c)=0\), and
\[
 f_*''(k)=\pi\Re\{3\cot\pi(a+ik)
              -\cot\pi(e_*+a+ik)-\cot\pi(s_*+a+ik)\}.
 \tag{16}
\]
On \([c,0]\), the derivative \(f_*'\) is convex.
Indeed
\[
 \partial_h\Re\cot\pi(x+ih)=
 -\frac{2\pi\sin(2\pi x)\sinh(2\pi h)}
 {\{\cosh(2\pi h)-\cos(2\pi x)\}^2}.
 \tag{17}
\]
The first argument in (16) is below the half angle with nonpositive
height. Both summed arguments are above the half angle with strictly
negative height. Differentiating (16) consequently gives
\(f_*'''>0\). For a summed argument \(x>1/2,h\le0\),
the original \(\arg(1-e^{2\pi h-2\pi ix})\) lies between
\(\pi(1/2-x)\) and zero. Hence
\[
 f_*'(0)<\frac{159\pi}{500},\qquad
 f_*(0)-f_*(c)<\frac{4293\pi}{250000}.
 \tag{18}
\]
The first inequality is
\(f_*'(0)\le\pi(1/2-a+\Re e_*-\Re s_*)
<\pi(.5+.363-.545)\).
The second integrates the chord of the convex derivative from its
zero at \(c\), using \(-c<27/250\).

Uniformly for \(0\le k\le H\), elementary cotangent bounds
give \(f_*''(k)<5\pi\). To retain the common \(a\), bound
its quotient by \(\pi\) by
\[
 3\cot(\pi a)-\cot\pi(a+.363)-\cot\pi(a+.45)<19/4<5.
 \tag{19}
\]
On \([.246,.30]\), the three terms are respectively less
than \(63/20,3/5,1\); on \([.30,.35]\) they are less
than \(9/4,1,3/2\). The needed elementary inequalities are
\(\cot(.246\pi)<21/20\), \(\cot(.30\pi)<3/4\),
\(\tan(.163\pi)<3/5\), and \(\tan(.30\pi)<3/2\).
For the first use
\(\cot(.246\pi)=(1+\tan(.004\pi))/(1-\tan(.004\pi))\)
and \(\tan(.004\pi)<13/1000\).
For the second and fourth use respectively
\(7/25<\cos(.4\pi)=\sin(.1\pi)<1/3\) and the
half-angle formulas. For the third use
\(.163\pi<.513\) and
\(.513/(1-.513^2/2)<3/5\).
The inequalities follow from \(3<\pi<22/7\),
\(\sin x\ge x-x^3/6\), \(\sin x\le x\), and
\(\cos x\ge1-x^2/2\); no numerical source test is involved.

It follows that \(f_*'(k)<97\pi/250\) on \([0,H]\).
Also \(\partial_k\Re g(a+ik)=-\arg(1-e^{2\pi k-2\pi ia})
<-3\pi/20\) there, while \(J(a)<-3/40\).
Consequently both actual branches obey
\[
 \begin{split}
 f_*(H)-2\pi H-f_*(c)&<-\frac{1349\pi}{250000}
                                      <-\frac1{100},\\
 f_*(H)+\Re g(a+iH)-f_*(c)
 &<\frac{2563\pi}{125000}-\frac3{40}<-\frac1{100}.
 \end{split}
 \tag{20}
\]
Here \(J(a)\le J(.35)<-3/40\) follows from
\(J'>1/2\) on \([.35,.5]\):
\(\sin(.35\pi)\ge\sin(21/20)>5/6\) by the lower
cubic sine bound, and
\(\log(5/3)>2\{(5/3)-1\}/\{(5/3)+1\}=1/2\).
The final comparisons in
(20) use \(3<\pi<22/7\).

This strictly controls a neighborhood of these fixed indices and the
first real reference coordinate, against the original cut plane.
It does not control the whole horizontal maximum in (2).
The nonnegative response term in (5) explains the additional
obligation. The sign argument for convex \(f_*'\) in this
subsection also uses \(\Im s_*<0\) and is not asserted for a
positive-height next type-three index. The conditional method in
Sections 1--3 has no such height-sign restriction.

## 5. The bound \(6\pi\) fails on the whole original horizontal box

The matrix target (11) cannot be proved by checking every point of the
old horizontal box, even for the factorial branch and a next type-four
vertex. This obstruction holds for every pair of actual private and
conditional heights allowed in (15). It does not assert that a
maximizer reaches the point used below.

Take the admissible target corner
\[
 \Re e=.49,\qquad \Re s=.5,\qquad \Re z=.45,\qquad k=H,
 \tag{21}
\]
with \(\Im e=h_e\in[-.051,-.019]\) and
\(\Im s=h_s\in[-.102,-.001]\). The outgoing real coordinate
and its fixed height are immaterial for the following diagonal entry.
The original phase gives
\[
 \begin{split}
 D:=\frac{-\mathcal F_{zz}}\pi
 &=3\cot\pi(.45+iH)+\cot\pi(.06+i v_e)
                    +\cot\pi(.05+i v_s)-i,\\
 v_e&=-h_e-H\in[.005,.037],\qquad
 v_s=-h_s-H\in[-.013,.088].
 \end{split}
 \tag{22}
\]
The final \(-i\) is required by the original \(g\) terms;
omitting it changes this test. For any positive definite real matrix
\(A\), Cauchy--Schwarz gives
\[
 (Cv)^TA^{-1}(Cv)\ge\frac{C_{zz}^2}{A_{zz}},\qquad
 A_{zz}+(Cv)^TA^{-1}(Cv)
 \ge\pi\left\{\Re D+\frac{(\Im D)^2}{\Re D}\right\}.
 \tag{23}
\]
Here \(v\) is the coordinate direction \(z\), and
\(A_{zz}=\pi\Re D>0\).

Write
\(\cot\pi(.06+i v_e)=a_e-i b_e\), with \(a_e,b_e>0\),
and put \(d_0=\cot(.12\pi)\). Elementary bounds give
\[
 3\Re\cot\pi(.45+iH)>2/5,\qquad d_0>5/2,
 \qquad a_e>d_0.
 \tag{24}
\]
For the last inequality, use
\(\cos(.12\pi)\cosh(2\pi v_e)
 <(19/20)(21/20)<1\).
The exact fixed-real-part cotangent circle identity is
\[
             (a_e-d_0)^2+b_e^2=d_0^2+1.
 \tag{25}
\]
Consequently, if \(b_e<2\), then
\(a_e>d_0+\sqrt{d_0^2-3}>21/5\).

Suppose first that \(v_s\ge0\). The last cotangent in
(22) has nonpositive imaginary part and
\[
 \Re\cot\pi(.05+i v_s)>
       \frac{3/10}{29/25-19/20}=\frac{10}{7}>\frac75.
 \tag{26}
\]
If \(b_e\ge2\), the imaginary part of the first cotangent
in (22) is strictly negative, so \(-\Im D>3\).
The expression in braces in (23) is at least
\(2|\Im D|>6\). If \(b_e<2\), equations (24)--(26)
instead give
\(\Re D>2/5+21/5+7/5=6\).
Thus in either case the effective curvature exceeds \(6\pi\).

If \(v_s<0\), its magnitude is at most \(.013\), and
\[
 \Re\cot\pi(.05+i v_s)>
                  \frac{3/10}{101/100-19/20}=5.
 \tag{27}
\]
Equations (24) and (27) already imply \(\Re D>6\),
without a restriction on \(b_e\). This finishes all height cases.

Here are elementary witnesses for the scalar bounds, so this test
needs no numerical source evaluation. Use
\(\sin(.1\pi)>3/10\), \(\cos(.1\pi)>19/20\),
\(\cos(.12\pi)<19/20\), and
\[
 \cosh(.176\pi)<29/25,\quad
 \cosh(.074\pi)<21/20,\quad
 \cosh(.028\pi),\ \cosh(.026\pi)<101/100.
 \tag{28}
\]
The sine and cosine bounds follow from \(157/50<\pi<22/7\)
and their alternating polynomials through degree four. The hyperbolic
bounds follow from
\(\cosh x\le1+x^2/2+x^4/[24(1-x^2/30)]\), at
\(x=111/200,233/1000,88/1000,82/1000\), respectively.
Finally, the upper sine polynomial through degree five divided by
\(1-x^2/2\), at \(x=66/175\), is less than \(2/5\);
this gives \(\tan(.12\pi)<2/5\) and \(d_0>5/2\).
All denominators displayed here are positive.

**Proposition 3.** At (21), the effective-curvature expression in
(11) is strictly greater than \(6\pi\) for every admitted
actual type-four pair of heights. If the full horizontal Hessian
were not positive definite at a point, the premise (3) would already
fail there; wherever it is positive definite, (23) proves the stated
obstruction. Strictness also gives nearby interior target points
with the same failure, so half-grid inward shifts do not remove it.

The conditional budget (13) remains valid along optimizing points.
To use it one must therefore enclose those points away from the
corner (21), prove a nonconstant integrated bound, or change the
private-height path and account for its new response. This is a
failure of the proposed uniform matrix bound on an overly large
target domain, not a positive defect of the selected source, and
not an actual-word counterexample.

## 6. An independent scalar credit does not pay the forced branch

Even a successful optimizing-point bound \(K_0\le6\pi\)
would not by itself control the forced branch on the whole first
plateau. Suppose the original height is bounded only by
\(c\ge-a_0\), where \(a_0=39/500\), or \(a_0=7/100\)
when the next vertex is type three. These are the bounds of the
[coupled height extraction](research_mixed_first_four_attached_height_bound.md),
not asserted values of particular words. Equation (12) would give
\[
                   G(H)\le M+3\pi(H+a_0)^2,
                 \qquad M=G(c).
 \tag{29}
\]
For \(H\ge0\), the real function \(\Re g(x+iH)\) is
strictly increasing on \(P=[.22,.45]\). Indeed its derivative
is \(\log|1-Re^{-2\pi ix}|\), \(R=e^{2\pi H}\ge1\);
the squared modulus increases with \(R\), and already at
\(R=1\) it is \(4\sin^2(\pi x)>1\). Thus replacing
the phase and factorial credit by independent suprema gives the
forced upper budget
\[
 M+C_{a_0}(H),\qquad
 C_a(H)=3\pi(H+a)^2+\Re g(9/20+iH).
 \tag{30}
\]
This budget is strictly positive for every \(a\ge7/100\)
and every \(H\ge0\). To see this, the original argument
\(A(H)=\arg(1-e^{2\pi H-9\pi i/10})\) lies between
zero and \(\pi/10\). Hence
\[
 C_a'(H)=6\pi(H+a)-A(H)>
                     \pi(6a-1/10)>0.
 \tag{31}
\]
Also \(J(9/20)>-(\log2)/20>-7/200\), using
\(\log2<7/10\). Therefore
\[
 C_a(H)\ge C_a(0)>
             9(7/100)^2-7/200=91/10000>0.
 \tag{32}
\]
The logarithmic bound follows, for example, because the exponential
series through degree four at \(7/10\) exceeds two.
Thus no nonnegative choice of selected height repairs this particular
scalar estimate. Equations (30)--(32) give no lower bound for the
true optimized phase: the two independent suprema need not be sharp
or attained at the same point.

The first real coordinate must instead be retained. Write the fixed
horizontal product as \(P\times K'\), with \(x\) the first
real coordinate and \(\xi\) the remaining ones, and set
\[
 G_x(x,H)=\max_{\xi\in K'}
  \{\Re\mathcal F(\xi,x;H)-\Re[p_b(b-b_*)]\}.
 \tag{33}
\]
Then the exact forced optimization is
\[
           \max_{x\in P}\{G_x(x,H)+\Re g(x+iH)\}.
 \tag{34}
\]
An optimizer enclosure or a quantitative support bound retaining
\(x\) can improve (30). No such forced-branch comparison is
inferred here. This is a limitation of the scalar upper-bound method,
not a failure of the original source or of every possible contour.

## 7. Positive-height restrictions for the forced maximum

Use the phase, domain and two objectives of the
[certified optimizer bounds](research_mixed_selected_boundary_optimizer_bounds.md),
with \(m\ge3\). In this section only,
\[
                    0\le k\le H=7/500.
 \tag{35}
\]
The conditional index \(s=s_2\) and outgoing coordinate \(b=t_2\)
belong to the same ordinary vertex, including when \(m=3\).
The [open factor indexing](research_mixed_open_local_factor_coverage.md)
therefore permits the full ordinary image bounds, rather than the
larger attached-endpoint rectangles:
\[
 h_s,h_b\in
 \begin{cases}
 [-.065,.068],&\epsilon=0,\\
 [-.102,-.001],&\epsilon=1.
 \end{cases}
 \qquad -.051\le h_e\le-.019.
 \tag{36}
\]
Both external inputs of that ordinary vertex may be attached; its
outputs \(s,b\) remain ordinary outputs. No private endpoint is used
as an input to an ordinary-image theorem.

**Proposition 4.** Every maximizer of either branch on the full
first-coordinate plateau \(x=\Re z\in P\) satisfies
\(\Re s>1/5\).

*Proof.* Write \(S_0=e^{-2\pi i s}\), \(Z=e^{-2\pi i z}\),
\(B=e^{-2\pi i b}\), and
\(r=|S_0|,\ R=|Z|,\ r_b=|B|\). At \(\Re s=1/5\),
the exact original marginal, including its chirp, gives
\[
 e^{2\Re\mathcal F_s}
 =\frac{|1-S_0Z|^2|1-S_0B|^2}
        {R^2|1-S_0|^{4+2\epsilon}}.
 \tag{37}
\]
Both shifted real arguments lie in \([.42,.65]\), whose
doubled-angle cosines are less than
\(-1/2\), while \(\cos(2\pi/5)>3/10\).
The heights give
\[
 \frac12<r<\frac85,\qquad r_b>\frac12,\qquad
 1\le R<\frac{11}{10};
 \quad\epsilon=1\ \Longrightarrow\ r<1.
 \tag{38}
\]
Consequently the right side of (37) is strictly greater than
\[
 \frac{N_1(r)N_2(r)}{D(r)^{2+\epsilon}},\quad
 N_1=r^2+\frac{10r}{11}+\frac{100}{121},\quad
 N_2=\frac{r^2}{4}+\frac r2+1,\quad
 D=r^2-\frac{3r}{5}+1.
 \tag{39}
\]
On \([1/2,8/5]\), the two concave quadratics
\[
 N_1-\tfrac32D=-\tfrac12r^2+\tfrac{199}{110}r-\tfrac{163}{242},
 \qquad
 N_2-\tfrac23D=-\tfrac5{12}r^2+\tfrac9{10}r+\tfrac13
 \tag{40}
\]
are positive at both endpoints and hence throughout the interval.
This proves (39) \(>1\) for \(\epsilon=0\).
For \(\epsilon=1\), \(D\le7/5\) and
\[
 N_2\ge21/16>98/75\ge(2/3)D^2;
 \tag{41}
\]
together with the first inequality in (40), this proves it for
\(\epsilon=1\) as well. Thus \(\Re\mathcal F_s>0\) at
\(\Re s=.2\).

This face sign also excludes the entire region below it. On
\(\ell_\epsilon\le\Re s\le.2\), where
\(\ell_0=.15,\ell_1=.125\), both \(\Re(s+z)\) and
\(\Re(s+b)\) lie in \([.345,.65]\). Each cotangent real
part is at most \(\cot(.345\pi)<3/5\): below real part
\(1/2\), an imaginary displacement can only decrease its positive
real part, and above \(1/2\) that real part is nonpositive.
The exact cotangent formula and
\(\cosh(.216\pi)<5/4\) give
\[
 \Re\cot\pi s>
 \frac{7/10}{5/4-3/10}=\frac{14}{19}.
 \tag{42}
\]
Here \(\sin(2\pi\Re s)>7/10\), and
\(\cos(2\pi\Re s)>3/10\), throughout that interval.
It follows directly that
\[
 \partial_{\Re s}\Re\mathcal F_s
 =\pi\Re\{\cot\pi(s+z)+\cot\pi(s+b)
                    -(2+\epsilon)\cot\pi s\}
 <-\frac{26\pi}{95}<0.
 \tag{43}
\]
Hence the marginal is positive whenever \(\Re s\le.2\).
Increasing \(\Re s\) a little is an admissible improvement at
every such point. The extra term distinguishing the two Fourier
branches is independent of \(s\), proving the assertion for both.

The elementary bounds in (38) require no new interval computation:
\(.204\pi<.65<2/3<\log2\),
\(.136\pi<.43\), and
\(e^x\le1+x+x^2/[2(1-x/3)]\) at \(x=.43\) gives
\(e^{.136\pi}<8/5\). The bound \(R<11/10\) is the
existing positive-height bound. The same cosine and hyperbolic
estimates used in the
[horizontal zero-mode proof](research_mixed_horizontal_zero_mode_support.md)
give (42); \(\tan(.155\pi)<3/5\) follows from
\(\sin t\le t,\ \cos t\ge1-t^2/2\) at \(t=341/700\).
\(\square\)

**Proposition 5.** If the second vertex is type three, every
maximizer of the forced branch on (35) has
\(\Re z<21/50=.42\).

*Proof.* The certified private-coordinate bound first gives
\(\Re e<.4\). Suppose \(x=\Re z\ge.42\) at a forced
maximizer. Proposition 4 gives \(\Re s>.2\).
The exact first-coordinate derivative is
\[
 e^{\partial_x f_{\rm force}}
   =\frac{|1-EZ|\,|1-S_0Z|}{|1-Z|^2|S_0|},
 \qquad E=e^{-2\pi i e}.
 \tag{44}
\]
In particular the factor \(|S_0|^{-1}\) from the original chirp
is retained. Now
\[
 |E|<\frac{89}{100},\quad |S_0|^{-1}<\frac{151}{100},\quad
 \cos(2\pi\Re(e+z))>-\frac{37}{100},\quad
 \cos(2\pi\Re(s+z))>-\frac{73}{100},\quad
 \cos(2\pi x)<-\frac78 .
 \tag{45}
\]
The real sum intervals are \([.69,.85)\) and \((.62,.95]\);
the last inequality holds on \(x\in[.42,.45]\).
Since \(R=e^{2\pi k}\ge1\), the square of (44) is less than
\[
 \frac{(\frac45R^2+\frac23R+1)
                   (R^2+\frac94R+\frac{23}{10})}
      {(R^2+\frac74R+1)^2}<1.
 \tag{46}
\]
Indeed denominator minus numerator is
\[
 P(R)=\frac15R^4+\frac{31}{30}R^3+\frac{289}{400}R^2
                      -\frac{17}{60}R-\frac{13}{10}
 \ge\frac{669}{400}R-\frac{13}{10}
 \ge\frac{149}{400}>0.
 \tag{47}
\]
The first inequality merely replaces each positive higher power
by \(R\), valid for \(R\ge1\).
Thus the real derivative is negative at the proposed maximum;
decreasing \(x\) slightly increases the objective in its original
product domain, a contradiction.

For completeness, all constants in (45) have elementary rational
witnesses. Use \(.038\pi>.119\) and
\(1+.119+.119^2/2>100/89\) for the first radius.
For the second use \(.13\pi<.41\) and the exponential upper
bound just used at \(x=.41\), which is less than \(151/100\).
The alternating sine upper polynomial through degree five at
\(66/175\) gives \(\sin(.12\pi)<37/100\).
The cosine upper polynomial through degree four at \(471/625\)
gives \(\cos(.24\pi)<73/100\).
The cosine lower polynomial through degree six at \(88/175\)
gives \(\cos(.16\pi)>7/8\). These use only
\(157/50<\pi<22/7\), and the monotonicity of the trigonometric
functions on the stated short intervals. \(\square\)

Both propositions are restricted to nonnegative first height.
They give no optimizer bound on the negative reset
\(c\le k<0\). Proposition 5 also uses the ordinary type-three
height bound; its radius estimate is not asserted for a type-four
second vertex. Neither proposition bounds the optimizing value
relative to the original reference, nor estimates a remaining
physical tail or connecting current.

## 8. Reduced curvature tests with the original optimizer equations

The now certified
[optimizer exclusions](research_mixed_selected_boundary_optimizer_bounds.md)
can be sharpened for the factorial branch without any further source
calculation. Throughout this section the selected height remains
\(H=7/500\). The ordinary next index is an output of the
full typed input map, even if one of that map's inputs is attached.
Thus Proposition 1 of the
[ordinary height theorem](research_mixed_cyclic_critical_height_bounds.md)
gives \(h_s>-.065\) for next type three and \(h_s>-.102\)
for next type four. This is an ordinary-index statement at every
length \(m\ge3\), not an assertion about an attached index.
In fact \(s=s_2\) and \(b=t_2\) are the two outputs of the
same ordinary vertex, so both \(h_s,h_b\) lie in
\([-.065,.068]\) for \(\epsilon=0\), and both lie in
\([-.102,-.001]\) for \(\epsilon=1\). See also Section 1 of
[the local factor coverage](research_mixed_open_local_factor_coverage.md).
These typed ranges may be imposed on the scalar tests below; they
do not release the remaining actual-reference correlations.

**Proposition 6.** Every factorial-branch horizontal maximizer in
the original box satisfies
\[
 \Re z<\begin{cases}3/8,&\epsilon=0,\\39/100,&\epsilon=1.
 \end{cases}
 \tag{48}
\]
No corresponding forced-branch bound is inferred from this assertion.

*Proof.* The certified private-coordinate bound gives \(\Re e<.4\).
Put \(R=e^{2\pi k}\), \(E=e^{-2\pi i e}\), and
\(S_0=e^{-2\pi i s}\). The exact real derivative is
\[
 \exp\{\partial_{\Re z}\Re\mathcal F\}
   =\frac{|1-EZ|\,|1-S_0Z|}{|S_0|\,|1-Z|^3},
       \qquad Z=e^{-2\pi i z}.
 \tag{49}
\]
The factor \(|S_0|^{-1}\) is the original chirp contribution.
At next type three, \(R>16/25\), \(|E|<9/10\), and
\(|S_0|^{-1}<8/5\). At \(\Re z=3/8\),
\(\Re(e+z)\in[.645,.775]\), so
\[
 |1-EZ|^2<1+\tfrac98R+\tfrac{81}{100}R^2,
 \quad |1-S_0Z|/|S_0|<\tfrac85+R,
 \quad |1-Z|^2>1+\tfrac75R+R^2.
 \tag{50}
\]
Here \(\cos(.29\pi)<5/8\) bounds the first cross term,
and \(\sqrt2>7/5\) bounds the last. The denominator minus
numerator after squaring (49) is bounded below by
\[
 \begin{split}
 P_3(R)&=(1+\tfrac75R+R^2)^3
       -(1+\tfrac98R+\tfrac{81}{100}R^2)(\tfrac85+R)^2\\
 &=R^6+\tfrac{21}5R^5+\tfrac{807}{100}R^4
   +\tfrac{7427}{1000}R^3+\tfrac{1379}{625}R^2
   -\tfrac{47}{25}R-\tfrac{39}{25}.
 \end{split}
 \tag{51}
\]
Its second derivative has positive coefficients, while
\(P_3(16/25)=478783521/244140625>0\) and
\(P_3'(16/25)=221679281/9765625>0\).

For next type four use \(R>3/5\) and the sharper ordinary
bound \(|S_0|^{-1}<19/10\). At \(\Re z=.39\),
the corresponding three bounds in (50) are
\[
 1+\tfrac{99}{100}R+\tfrac{81}{100}R^2,
       \qquad \tfrac{19}{10}+R,
       \qquad 1+\tfrac{77}{50}R+R^2.
 \tag{52}
\]
They use \(\cos(.32\pi)<11/20\) and
\(\cos(.22\pi)>77/100\). Their difference polynomial is
\[
 \begin{split}
 P_4(R)&=(1+\tfrac{77}{50}R+R^2)^3
 -(1+\tfrac{99}{100}R+\tfrac{81}{100}R^2)(\tfrac{19}{10}+R)^2\\
 &=R^6+\tfrac{231}{50}R^5+\tfrac{11631}{1250}R^4
 +\tfrac{1103033}{125000}R^3+\tfrac{24287}{10000}R^2
 -\tfrac{27539}{10000}R-\tfrac{261}{100}.
 \end{split}
 \tag{53}
\]
Again \(P_4''\) has positive coefficients;
\(P_4(3/5)=1014393/7812500>0\) and
\(P_4'(3/5)=132440077/6250000>0\).
Thus (49) is strictly below one at either proposed cut.
Above that cut, both summed arguments \(e+z,s+z\)
have real parts between one half and one, while \(z\) has
real part below one half. Consequently
\(\Re\mathcal F_{zz}<0\), so the derivative remains negative.
Decreasing \(\Re z\) slightly is an admissible improvement
in the original box. This excludes every point claimed in (48).

For completeness, all scalar constants used here have elementary
rational witnesses. With \(25/8<\pi<22/7\), the inequality
\(e^x\le1+x+x^2/[2(1-x/3)]\) at \(x=11/25\)
and \(396/875\) gives respectively
\(e^{.14\pi}<25/16\) and \(e^{.144\pi}<8/5\).
The same bound at \(429/875\) gives
\(e^{.156\pi}<5/3\). Also
\[
 \sum_{j=0}^{5}\frac{(561/875)^j}{j!}
 +\frac{(561/875)^6}{6!(1-(561/875)/7)}<\frac{19}{10}
 \tag{54}
\]
proves \(e^{.204\pi}<19/10\). The cosine upper polynomial
through degree four at \(29/32\) is less than \(5/8\);
the same polynomial at one is \(13/24<11/20\).
The cosine lower polynomial through degree six at \(121/175\)
is greater than \(77/100\). Monotonicity of cosine on the
relevant interval gives all the stated trigonometric bounds.
Finally \(|E|<9/10\) follows from
\(e^{.038\pi}>1+.038\pi>10/9\).
These are finite rational comparisons, not new root or source
certificates. \(\square\)

The effective curvature in Lemma 1 has a particularly simple scalar
form for this phase. Define the following *complex* cotangents,
with the factor \(\pi\) understood inside each argument:
\[
 \begin{gathered}
 p_e=\cot(\pi e),\quad p_s=\cot(\pi s),\quad
 p_z=\cot(\pi z),\quad p_b=\cot(\pi b),\\
 d=\cot\pi(e+z),\quad f=\cot\pi(s+z),\quad
 g_0=\cot\pi(s+b),\quad \sigma=-S''(e)/\pi.
 \end{gathered}
 \tag{55}
\]
In the order \((e,s,z,b)\), the normalized complex matrix
\(\mathsf H=-\mathcal F''/\pi\) has diagonal
\[
 \sigma+p_e-d-i,\quad
 (2+\epsilon)p_s-f-g_0-i\epsilon,\quad
 3p_z-d-f-i,\quad
 (1+\epsilon/2)p_b-g_0-i\epsilon/2,
 \tag{56}
\]
and its only nonzero off-diagonal entries are
\(\mathsf H_{ez}=-d+i\),
\(\mathsf H_{sz}=-f-i\), and
\(\mathsf H_{sb}=-g_0+i\).
These signs use \(g''(v)=\pi\cot(\pi v)-i\pi\)
and retain both original quadratic chirps.

Set
\[
 \begin{gathered}
 E_0=\Re(\sigma+p_e-d),\quad
 B_0=\Re((1+\epsilon/2)p_b-g_0),\\
 T_0=\Re((2+\epsilon)p_s-f-g_0)
                -\frac{(\Re g_0)^2}{B_0},\qquad
 a_0=\Re(3p_z-d-f),\\
 b_e=-\Re d,\quad b_s=-\Re f,\quad
 q_e=1-\Im d,\quad q_s=-1-\Im f,\\
 q_z=\Im(3p_z-d-f)-1,\qquad
 D_0=a_0-b_e^2/E_0-b_s^2/T_0.
 \end{gathered}
 \tag{57}
\]
When \(E_0,B_0,T_0,D_0>0\), the negative real Hessian
\(A=-\Re\mathcal F''\) is positive definite. Conversely, its
positive definiteness implies
these four inequalities. Successive real Schur complements give the
exact identity
\[
 \frac{K_{\rm eff}}\pi
 =a_0+\frac{q_e^2}{E_0}+\frac{q_s^2}{T_0}
 +\frac{(q_z-b_eq_e/E_0-b_sq_s/T_0)^2}{D_0}.
 \tag{58}
\]
Here \(K_{\rm eff}=v^TAv+(Cv)^TA^{-1}(Cv)\) is the
upper expression in (5), with \(v\) the \(z\) direction.
If \(b\) is held fixed rather than optimized, remove its row
and column and use
\(T_0=\Re((2+\epsilon)p_s-f-g_0)\); the rest is unchanged.
At an active face (58) is still the same valid upper bound from
Lemma 1, although the actual optimizing response can be smaller.
For the forced phase, replace \(a_0\) by
\(a_0-\Re p_z\) and \(q_z\) by
\(q_z-\Im p_z+1\), and check positivity again.

One should impose the original optimizer equations before attempting
to bound (58). Let \(W=e^{-2\pi i u_c(e)}\), where
\(u_c(e)\) is the canonical cap root, and let
\(B=e^{-2\pi i b}\). Write \(D_e=\partial_{\Re e}\Re\mathcal F\) and
\(D_s=\partial_{\Re s}\Re\mathcal F\), and let
\(D_{z,\rm fac}\), \(D_{z,\rm force}\) be the corresponding
first-coordinate derivatives for the two branches. Directly from
the original logarithmic derivatives,
\[
 \begin{split}
 e^{D_e}&=\frac{|1-EZ|}{|1-E|\,|W-E|},\\
 e^{D_s}&=\frac{|1-S_0Z|\,|1-S_0B|}
                  {|Z|\,|1-S_0|^{2+\epsilon}},\\
 e^{D_{z,\rm fac}}&=
 \frac{|1-EZ|\,|1-S_0Z|}{|S_0|\,|1-Z|^3},
 \qquad e^{D_{z,\rm force}}=e^{D_{z,\rm fac}}|1-Z|.
 \end{split}
 \tag{59}
\]
Here \(S_0=e^{-2\pi i s}\) is still the exponential
variable from (49). For the first identity, substitute
\(S'(e)=-\log(2\sin\pi(e-u_c(e)))+i\pi u_c(e)\)
and use the original log-sine identity. Its exponential before
taking modulus is
\((1-EZ)/[(1-E)(W-E)]\), so there is no added log-lift
assumption in this necessary real equation.

At any maximum, each coordinate strictly above its original lower
face has nonnegative real derivative; if it is also below its
original upper face, that derivative vanishes. Thus the appropriate
ratio in (59) must be at least one, and is exactly one at an
interior coordinate. A whole target cell strictly above a lower
face on which its ratio is bounded strictly below one contains no
maximizer. The same statement holds with the upper-face sign
reversed. This is a necessary optimizer exclusion, not a sufficient
geometric-reference test. In particular it can remove high-curvature
points that survive the rectangular bounds (48).

Neither the positivity premises of (58) nor an upper curvature
constant along all surviving maxima is asserted here. The formulas
reduce that question to scalar quantities with their original
correlations; they do not establish a calibrated selected-source
gap, the forced-branch initial budget, or any missing current bound.

## 9. An analytic private-coordinate lower barrier at positive height

Continue with the actual ordinary heights of (36), the original
horizontal box, and \(0\le k\le H=7/500\).
All four real variables \(\Re e,\Re s,\Re z,\Re b\) range over
the original horizontal box, while \(h_e,h_s,h_b\) stay fixed at
their actual reference values. The lower barrier below, like Section 7,
is not asserted on the negative reset.

**Proposition 7.** Every maximizer of either Fourier branch satisfies
\(\Re e>3/10\).

*Proof.* Let \(D_e=\partial_{\Re e}\Re\mathcal F\).
At \(\Re e=.3\), the real sum \(e+z\) ranges from
\(.52\) to \(.75\), so
\(\partial_{\Re z}D_e=\pi\Re\cot\pi(e+z)<0\).
Its minimum in \(\Re z\) is therefore at \(\Re z=.45\).
At that value the real sum is \(.75\), and
\[
 \partial_kD_e
   =\pi\{1-\Im\cot\pi(.75+i(h_e+k))\}>0.
 \tag{60}
\]
Indeed the imaginary cotangent equals
\(-\tanh(2\pi(h_e+k))\). It suffices to prove
\(D_e>0\) at \(e=.3+ih_e,\ z=.45\).

Put
\[
 E=e^{-2\pi ie}=r(-\gamma-i\sin(.4\pi)),\quad
 \gamma=\cos(.4\pi),\quad \delta=\cos(.2\pi),\quad
 D=\sqrt{E(2-E)}.
 \tag{61}
\]
Here \(7/10<r<9/10,\ 3/10<\gamma<31/100\), and
\(\delta>4/5\). The square root has positive real part and
negative imaginary part. Its compatibility with the original cap
branch can be checked directly, without selecting a new root.
Let \(W_0=\sqrt{1-2/E}\) be the square root in the canonical
\(u_c(e)\) formula. Its argument lies in \((-\pi/4,0)\),
so \(D=iEW_0\) has argument in
\((-7\pi/20,-\pi/10)\). For
\(V=e^{-2\pi i u_c(e)}=(3-iW_0)/(1+iW_0)\), substitution gives
\[
 V=\frac{E+1-2D}{E-1},\qquad
 (1-E)(V-E)=-(1-D)^2,\qquad
 e^{D_e}=\frac{\sqrt{1+r^2}}{|1-D|^2}.
 \tag{62}
\]
The last identity is the original endpoint modulus equation (59);
\(EZ=ir\) at this real pair. In particular no logarithmic
lift is changed.

Write \(L=|D|^2\) and \(A=\Re(D^2)\). Then
\[
 L=r\sqrt{4+4\gamma r+r^2}\ge2r+\gamma r^2,\qquad
 A=\delta r^2-2\gamma r,\qquad
 2\Re D=\sqrt{2L+2A}.
 \tag{63}
\]
The exact square of \(L\), together with the displayed bounds
for \(\gamma,\delta\), implies
\[
 \begin{split}
 2L+2A-(L-\tfrac15)^2
 &\ge q(r),\\
 q(r)&=-r^4-\tfrac{31}{25}r^3-\tfrac{42}{25}r^2
                          +\tfrac{89}{25}r-\tfrac1{25}>0 .
 \end{split}
 \tag{64}
\]
To verify the last sign, \(q''(r)<0\) for \(r>0\), and
\(q(7/10)=48169/50000\),
\(q(9/10)=12157/50000\). Concavity therefore proves positivity
on the whole required radius interval. Since \(L>7/5\),
(64) can be square-rooted with the indicated sign. It gives
\[
 |1-D|^2=1+L-2\Re D<6/5,\qquad
 e^{D_e}>\frac{\sqrt{149}}{12}>1 .
 \tag{65}
\]
This proves the strictly positive derivative at the reduced pair.
The joint cap concavity used in Proposition 1 of the certified
optimizer note makes \(D_e\) decrease with \(\Re e\).
Thus \(D_e>0\) throughout \(\Re e\le.3\).
Increasing that coordinate slightly is an admissible improvement
of either objective and excludes the entire lower region.

The radius bounds in (61) are elementary:
\(.102\pi<.33\), and the exponential upper bound from Section 7
at \(x=.33\) is less than \(10/7\);
\(.038\pi>1/9\) gives \(e^{-.038\pi}<9/10\).
The exact values
\(\gamma=(\sqrt5-1)/4,\ \delta=(\sqrt5+1)/4\)
give the remaining rational bounds. \(\square\)

**Corollary 8.** For a type-three second vertex, the forced
optimizer bound in Proposition 5 improves to
\(\Re z<41/100\), still only for \(0\le k\le H\).

*Proof.* If \(x=\Re z\ge.41\) at a maximum, Proposition 4
gives \(\Re s>.2\), and Proposition 7 together with the
certified upper barrier gives \(.3<\Re e<.4\).
Thus the real sum intervals are now
\(\Re(e+z)\in(.71,.85)\) and
\(\Re(s+z)\in(.61,.95]\). In (44), retain
\(|E|<89/100,\ |S_0|^{-1}<151/100\), and use
\[
 \cos(2\pi\Re(e+z))>-1/4,\quad
 \cos(2\pi\Re(s+z))>-4/5,\quad
 \cos(2\pi x)<-21/25.
 \tag{66}
\]
The square of the exact forced derivative ratio is therefore less
than
\[
 \frac{(\frac45R^2+\frac9{20}R+1)
                (R^2+\frac{49}{20}R+\frac{23}{10})}
      {(R^2+\frac{42}{25}R+1)^2}<1,\qquad R\ge1 .
 \tag{67}
\]
The denominator minus numerator equals
\[
 \frac15R^4+\frac{19}{20}R^3+\frac{8799}{10000}R^2
                       -\frac18R-\frac{13}{10}
 \ge\frac{19049}{10000}R-\frac{13}{10}
 \ge\frac{6049}{10000}>0 .
 \tag{68}
\]
Thus decreasing \(x\) slightly increases the forced objective,
contradicting maximality. The trigonometric constants in (66)
follow respectively from the sine upper polynomial through degree
five at \(44/175\), the cosine upper polynomial through degree
four at \(1727/2500\), and the cosine lower polynomial through
degree six at \(99/175\), using \(157/50<\pi<22/7\).
\(\square\)

These are restrictions of the optimizing location, not a calibrated
bound for its value. They do not establish the remaining matrix
bound, the negative-height reset, or any omitted finite current.
Corollary 8 uses the actual ordinary type-three height bound. A separate
type-four estimate follows next.

**Corollary 9 (the type-four forced ceiling).**

Under the hypotheses of Proposition 7, if the next vertex is type
four then every forced maximizer has \(\Re z<87/200\).
Indeed if \(x\ge87/200\), Proposition 4 gives
\(\Re s>.2\), and the private barriers give \(.3<\Re e<.4\).
Thus
\[
 \cos(2\pi\Re(e+z))>-1/10,\qquad
 \cos(2\pi\Re(s+z))>-2/3,\qquad
 \cos(2\pi x)<-9/10 .
 \tag{69}
\]
These follow from
\(\sin(.03\pi)<1/10,\ \cos(.27\pi)<2/3\), and
\(\cos(.13\pi)>9/10\), using the same elementary sine and
cosine polynomials. With \(|E|<.89\) and
\(|S_0|^{-1}<19/10\), the square of the forced derivative
ratio in (44) is less than
\[
 \frac{(\frac45R^2+\frac9{50}R+1)
                (R^2+\frac{13}{5}R+\frac{73}{20})}
      {(R^2+\frac95R+1)^2}<1,\qquad R\ge1 .
 \tag{70}
\]
The denominator minus numerator is
\[
 \frac15R^4+\frac{67}{50}R^3+\frac{213}{250}R^2
                 +\frac{343}{1000}R-\frac{53}{20}
 \ge\frac{547}{200}R-\frac{53}{20}
 \ge\frac{17}{200}>0 .
 \tag{71}
\]
The real derivative is therefore negative, excluding every such
point by an admissible decrease of \(x\). This location bound by
itself supplies no forced-value gap for the next-four case.

**Conditional common-gap consequence for a three-type neighbor.**

Suppose the next vertex is type three, the actual first height obeys
\(c\ge-.07\), and the hypotheses of Lemma 1 and (10)--(11)
hold for the original phase \(\mathcal F\) on its fixed horizontal
domain throughout \([c,1/100]\), with \(K_0\le6\pi\).
Then at the alternative selected height \(H_0=1/100\) both
Fourier branches have maximum strictly below
\(M-1/500\), where \(M=G(c)\).

For the factorial branch, (12) gives
\[
 G(H_0)-2\pi H_0-M
 \le3\pi(2/25)^2-\pi/50
 =-\pi/1250<-1/500 .
 \tag{72}
\]
For the forced branch, Corollary 8 puts every maximizing
first coordinate below \(.41\). Since \(\Re g(x+iH_0)\)
increases with \(x\in P\), the exact maximization is at most
\[
 G(H_0)+\Re g(.41+iH_0).
 \tag{73}
\]
The positive-height argument lower bound gives
\(\Re g(.41+iH_0)\le J(.41)-9\pi/10000\).
The function \(J'(x)=\log(2\sin\pi x)\) is concave on
\([.41,.5]\), and its endpoint values exceed \(13/20\)
and \(69/100\), respectively. Hence
\[
 J(.41)<-\frac9{200}\left(\frac{13}{20}+\frac{69}{100}\right)
         =-\frac{603}{10000}.
 \tag{74}
\]
For explicit elementary witnesses,
\[
 e^{13/20}
 \le1+\frac{13}{20}+\frac{(13/20)^2}{2}
       +\frac{(13/20)^3}{6(1-13/80)}
 <\frac{235199}{122500}
 <2\cos(.09\pi),
 \tag{75}
\]
and the positive series
\(2(1/3+1/81+1/1215)>69/100\) is a lower bound for
\(\log2\). Concavity of \(J'\) bounds its integral below
by the trapezoid with these two endpoint bounds.
Consequently
\[
 \max f_{\rm force}-M
 <\frac{183\pi-603}{10000}
 <-\frac{39}{14000}<-1/500 .
 \tag{76}
\]

Unlike the independent full-plateau scalar estimate in Section 6,
this comparison retains a proved restriction on the forced
maximizer before spending its factorial credit. The effective-curvature
hypothesis is still unproved, and this conclusion concerns the two
central phase maxima only. No private real tail, alias, connecting
current, or whole-source theorem is inferred. The graph height
\(H_0\) is an alternative exact selected contour parameter, not a
claim that earlier source estimates automatically transfer to it.

## 10. Conditional interior flow on the positive-height segment

The preceding scalarization also gives a precise, limited statement
about the motion of a maximizing point. This statement concerns the
original phase \(\mathcal F\), equivalently its factorial branch:
subtracting \(2\pi k\) does not change its horizontal maximizer.
It does not apply unchanged to the forced phase.

Let \(I\subset[0,H]\), \(H=7/500\), be an interval on which
the hypotheses of Lemma 1 hold, the maximizing point is in the
interior of the original four-variable horizontal box, and its
negative real Hessian is positive definite. Write the real maximizing
coordinates as \(e_R(k),s_R(k),z_R(k),b_R(k)\). Their imaginary
parts other than \(k\) remain fixed at the actual reference values.
Assume throughout this interval that
\[
 \Re(e+z),\ \Re(s+z),\ \Re(s+b)\in(1/2,1),
 \qquad 0<\Im d<1,\qquad q_s=-1-\Im f<0,
 \tag{77}
\]
where \(d,f\) and all matrix quantities are those of (55)--(57).
These are explicit additional conditions, not an assertion that the
actual maximizing path preserves this region.

**Proposition 10.** Under these hypotheses,
\[
             z_R'<0,\qquad e_R'>0,\qquad (s_R+z_R)'<0.
 \tag{78}
\]
No sign for \(s_R'\) alone follows from this argument.

*Proof.* Interiority and the implicit function theorem give
\(x'=A^{-1}Cv\). Put \(j=-\Re g_0>0\), and use the
normalized quantities of Section 8. Since \(\Re s\le1/2\)
and \(\Re b<1/2\),
\[
 T_0-b_s=(2+\epsilon)\Re p_s
    +\frac{j(1+\epsilon/2)\Re p_b}{B_0}>0.
 \tag{79}
\]
Here \(B_0=(1+\epsilon/2)\Re p_b+j\).
The three regular-sum conditions make \(b_e,b_s,j\) positive.
Let \(v_e=\Im d\), \(v_z=\Im p_z\). Nonnegative
\(k\) gives \(v_z\le0\). In the actual height range
\(h_e+k<0\), so \(v_e>0\), consistently with (77).
The remaining explicit signs in (77) give
\[
 \begin{split}
 Q&:=q_z-b_eq_e/E_0-b_sq_s/T_0\\
  &=3v_z+q_s(1-b_s/T_0)-v_e
                    -\frac{b_e(1-v_e)}{E_0}<0.
 \end{split}
 \tag{80}
\]
The Schur solution for the derivatives is
\[
 \begin{split}
 z_R'&=Q/D_0,\qquad
 e_R'=(q_e-b_ez_R')/E_0,\\
 s_R'&=(q_s-b_sz_R')/T_0,\qquad
 b_R'=-j s_R'/B_0.
 \end{split}
 \tag{81}
\]
Positivity of the Schur denominators proves the first two signs
in (78). The third is immediate from
\[
       (s_R+z_R)'=
          \{q_s+(T_0-b_s)z_R'\}/T_0<0.
 \tag{82}
\]
This proves the proposition. \(\square\)

For clarity, the unresolved separate \(s_R'\) sign has an exact
scalar criterion. Define
\[
 \beta=b_e/E_0,\quad
 \alpha=v_e+\beta(1-v_e)-3v_z>0,\quad
 L=3\Re p_z+b_e(1-\beta).
 \tag{83}
\]
Equations (80)--(81) reduce to
\[
 s_R'=\frac{q_s L+b_s\alpha}{T_0D_0},\qquad
 s_R'<0\quad\Longleftrightarrow\quad
                  \frac L\alpha>\frac{b_s}{-q_s}.
 \tag{84}
\]
The last ratio retains the summed height exactly. If
\(T=s_R+z_R\) and \(\rho=e^{2\pi(h_s+k)}\), then
\[
 \frac{b_s}{-q_s}
     =\frac{-\rho\sin(2\pi T)}{1-\rho\cos(2\pi T)}.
 \tag{85}
\]
Its denominator is positive by \(q_s<0\). At \(k=0\)
for a next type-four vertex, \(h_s<0\) and hence \(\rho<1\);
then this ratio is at most \(-\cot(\pi T)\). That particular
bound is not asserted when the summed height is positive.

In particular, a proposed proof based on \(z_R'\ge0\) cannot
apply to an interior maximizing segment satisfying (77), including
its one-sided limit at height zero. This is a conditional flow
calculation, not a located counterexample to an actual source or
an existence statement for such a segment. The negative-height
reset, preservation of (77), possible active-face transitions, and
the required effective-curvature bound remain separate obligations.

## 11. An algebraic numerator for the remaining curvature inequality

Keep the definitions in (55)--(58) and a positive horizontal Hessian.
For a dimensionless proposed bound \(\varkappa\), define
\[
 \begin{split}
 D_{\rm num}&=a_0E_0T_0-b_e^2T_0-b_s^2E_0,\\
 Q_{\rm num}&=q_zE_0T_0-b_eq_eT_0-b_sq_sE_0,\\
 M_{\varkappa}&=(\varkappa-a_0)E_0T_0
                                  -q_e^2T_0-q_s^2E_0,\\
 \mathfrak N_{\varkappa}&=M_{\varkappa}D_{\rm num}-Q_{\rm num}^2.
 \end{split}
 \tag{86}
\]
Here \(E_0,T_0,D_{\rm num}\) are strictly positive, since
\(D_{\rm num}=E_0T_0D_0\). Equation (58) gives exactly
\[
 \varkappa-\frac{K_{\rm eff}}\pi
       =\frac{\mathfrak N_{\varkappa}}{E_0T_0D_{\rm num}}.
 \qquad
 K_{\rm eff}\le\varkappa\pi
       \ \Longleftrightarrow\ \mathfrak N_{\varkappa}\ge0.
 \tag{87}
\]
This equivalence is used only with those positive denominators.
When \(b\) is optimized, \(B_0>0\) is also required to
define the real Schur complement \(T_0\). The forced version
uses the replacements after (58) and its own positive pivots.

Every coefficient in (86) is a real rational expression in the
exponentials \(E,S_0,Z,B,W\) and their complex conjugates.
The only term requiring explanation is \(\sigma=-S''(e)/\pi\).
Use different letters from the outgoing coordinate \(b\):
\[
 \eta=\cot\pi(e-u_c(e)),\qquad
 \xi=2\tan\pi u_c(e)+3\cot\pi u_c(e).
 \tag{88}
\]
For the original unoptimized endpoint phase, its \(ee,eu,uu\)
second derivatives are respectively
\(-\pi\eta,\ \pi(\eta+i),\ -\pi(\xi+\eta)\).
The canonical inner critical point is simple on the original cap
rectangle, as in the
[cap phase theorem](research_mixed_first_cap_plateau_phase.md).
Implicit differentiation and the complex Schur complement therefore
give
\[
 u_c'(e)=\frac{\eta+i}{\xi+\eta},\qquad
 \sigma=\eta-\frac{(\eta+i)^2}{\xi+\eta}.
 \tag{89}
\]
All these quantities are rational in the exponentials: for
\(Q=e^{-2\pi i v}\),
\(\cot(\pi v)=i(1+Q)/(1-Q)\) and
\(\tan(\pi v)=-i(1-Q)/(1+Q)\). In particular
\(\eta=i(W+E)/(W-E)\), while \(\xi\) is rational in
\(W\).

The canonical \(W=e^{-2\pi i u_c(e)}\) obeys
\[
             (E-1)W^2-2(E+1)W+5E-1=0.
 \tag{90}
\]
Indeed the original explicit root formula gives
\(2E\tan^2(\pi u_c)-2iE\tan(\pi u_c)-E+1=0\).
Substituting \(\tan(\pi u_c)=-i(1-W)/(1+W)\)
gives (90). This polynomial is not a replacement for branch
selection: \(W\) is still the canonical root fixed by the
original endpoint packet and its logarithmic lift. Its discriminant
is \(16E(2-E)\), which does not vanish on the present cap
domain. The other algebraic root is not admitted merely because it
satisfies (90).

The original regular strips ensure nonvanishing of the denominators
\(1-E,1-S_0,1-Z,1-B,1-EZ,1-S_0Z,1-S_0B,1-W,1+W,W-E\).
The existing cap chamber gives \(\Re\xi>2\) and
\(\Re\eta>1/42\), hence \(\xi+\eta\ne0\).
After expressing real and imaginary parts using conjugates, their
denominators can be cleared by strictly positive squared moduli;
the admitted positive real Schur pivots can likewise be cleared
without changing signs. Thus (87), the squared modulus conditions
(59), and the real and imaginary parts of (90) give an explicit
real algebraic sign problem. No dilogarithm evaluation is needed for
this curvature test.

The outgoing tangent can also be retained algebraically. Let stars
denote the original critical reference exponentials, and subtract
its fixed \(\Re p_b\) from the real \(b\) derivative.
That unsubtracted derivative is
\(\log|1-S_0B|-(1+\epsilon/2)\log|1-B|\).
Consequently interior \(b\)-stationarity and the three unchanged
heights imply
\[
 \begin{gathered}
 |1-S_0B|^4\,\bigl(|1-B_*|^2\bigr)^{2+\epsilon}
   =|1-S_*B_*|^4\,\bigl(|1-B|^2\bigr)^{2+\epsilon},\\
 |E|^2=|E_*|^2,\qquad |S_0|^2=|S_*|^2,
                    \qquad |B|^2=|B_*|^2.
 \end{gathered}
 \tag{91}
\]
Here \(S_*=e^{-2\pi i s_*}\), consistent with the exponential
\(S_0\), rather than the endpoint action \(S\).
The first equation follows by exponentiating and taking the fourth
power of a positive modulus ratio; all its powers are polynomial
in squared moduli. At a boundary face it is replaced by the
corresponding derivative-sign inequality. These constraints preserve
the actual reference tangent and heights instead of replacing them
by independent extrema.

No positivity of \(\mathfrak N_{\varkappa}\) is proved here.
The original reference compatibility, canonical root, fixed heights,
optimizer face conditions, and positive-pivot hypotheses must all be
retained. This local algebraic reduction identifies neither a knot
polynomial nor a nonzero source contribution, and replaces none of
the remaining finite-current estimates. Algebraic dependence or
Zariski density alone does not establish the required real inequality.

## 12. Whole-reset enclosures and the actual concavity hypotheses

The actual-reference bounds in (36) also permit two useful extensions
to the negative reset. Keep \(m\ge3\), the original outgoing
tangent, and the fixed actual heights \(h_e,h_s,h_b\). Let
\(c\) be the actual first height, so \(c>-.070\) for next
type three and \(c>-.078\) for next type four. Throughout
\(c\le k\le H=7/500\), the following statements hold:
\[
 \begin{array}{ll}
 \Re s>1/5&\text{at every maximizer of either branch},\\
 3/10<\Re e<2/5&\text{at every factorial-branch maximizer}.
 \end{array}
 \tag{92}
\]
The negative-height lower bound on \(e\) is not asserted for the
forced branch.

For the first statement, the proof of Proposition 4 uses only
\(0<R<11/10\), not its previously stated lower bound
\(R\ge1\). In fact the first numerator estimate is
\[
 \frac{|1-S_0Z|^2}{R^2}
 >r^2+\frac rR+\frac1{R^2}
 \ge r^2+\frac{10r}{11}+\frac{100}{121}.
 \tag{93}
\]
It remains valid when \(k<0\). The lower-\(s\) cotangent estimate
(43) depends on the real strips and \(h_s\), not on the shifted
height \(h_s+k\). Thus the same strictly positive marginal
excludes the entire region \(\Re s\le.2\) for both branches
throughout the reset.

For the second statement, Proposition 6 already gives
\(\Re z<.39\) for either next type on the whole reset interval.
Its proof uses the private upper barrier only, so there is no
circular use of the new lower barrier. At \(\Re e=.3\),
the real sum \(e+z\) lies in \([.52,.69)\), and consequently
\(\cos(2\pi\Re(e+z))<-7/20\).
Also \(r=|E|>7/10\) and \(R>3/5\). The canonical denominator
bound from (65) depends only on \(e\), so it remains valid at
negative \(k\). The exact marginal (59) gives
\[
 |1-EZ|^2>
   1+(21/50)^2+(7/10)(21/50)=\frac{919}{625}
       >\frac{36}{25},\qquad
 e^{D_e}>\frac{\sqrt{919}}{30}>1.
 \tag{94}
\]
Here \(\sin(.12\pi)>\sin(3/8)>
3/8-(3/8)^3/6=375/1024>7/20\) proves the cosine bound.
Cap concavity extends the positive marginal to \(\Re e\le.3\),
excluding that region. The previously certified upper barrier gives
the other side of (92).

These enclosures also discharge the concavity and initial-reference
hypotheses used in the conditional common-gap consequence.
Replace the original horizontal box by the fixed box with
\(\Re s\in[.2,.5]\), leaving its other intervals unchanged.
The first part of (92) shows that this replacement changes neither
maximum, at any height in the reset interval.

On this smaller box all ordinary arguments \(s,z,b\) have
real part at least \(.2\), absolute height at most \(.108\),
and real part at most \(1/2\). The latter is strictly less than
\(1/2\) for \(z,b\). The cotangent formula implies
\[
 \Re\cot\pi s\ge0,\quad
 \Re\cot\pi z,\Re\cot\pi b>0,\qquad
 |\Im\cot\pi s|,|\Im\cot\pi z|,|\Im\cot\pi b|<1.
 \tag{95}
\]
Indeed the last inequality is equivalent to
\(\cos(2\pi\Re v)<e^{-2\pi|\Im v|}\).
Here its left side is at most \(\cos(.4\pi)<1/3\), while
its right side exceeds \(e^{-.216\pi}>1/2\).

To include the face \(\Re s=1/2\) explicitly, let the two
cotangents of one pair be \(a+ib,c+id\), with
\(a\ge0,c>0,|b|,|d|<1\). For
\(V(v,w)=g(v+w)-g(v)-g(w)\), the exact pair determinant is
\[
 \det(-\Re V''/\pi)
 =\frac{(a+c)^2-(cb-ad)^2}{(a+c)^2+(b+d)^2}>0 .
 \tag{96}
\]
The numerator is positive because
\(|cb-ad|\le c|b|+a|d|<a+c\), including \(a=0\).
If \(C=\Re\cot\pi(v+w)\), the same determinant equals
\(ac-(a+c)C\). Thus \(C<ac/(a+c)\), and both diagonal
entries \(a-C,c-C\) are positive. Each of
\(-\Re V(s,z)''\) and \(-\Re V(s,b)''\) is therefore
positive definite; compactness makes these bounds uniform.

Let \(\Psi_1\) be the original bare first-cap phase:
\[
 \begin{split}
 \Psi_1(e,z)&=S(e)+g(e+z)-g(z)-g(e)
                         -\frac{i\pi}{2}(e-e^2),\\
 \mathcal F&=\Psi_1(e,z)+V(s,z)+V(s,b)
        -\epsilon g(s)-g(z)-\frac{\epsilon}{2}g(b)+2\pi izs .
 \end{split}
 \tag{97}
\]
The [whole cap Hessian proof](research_mixed_first_cap_plateau_phase.md)
gives \(-\Re\Psi_1''\succ(\pi/200)I_2\) on its stated
rectangle, which contains all the present \(e,z\).
The extra negative \(g\) terms in (97) have nonnegative
negative real Hessians by (95), and the chirp has zero real
Hessian. The cap pair controls the \((e,z)\) directions and
the ordinary pair \(V(s,b)\) controls \((s,b)\).
Their sum is uniformly positive definite on the four-variable box.
For the forced phase \(\mathcal F+g(z)\), only the displayed
\(-g(z)\) term is removed, so the same conclusion holds.
Subtracting the outgoing affine tangent changes neither Hessian.

Finally the actual original critical reference lies strictly inside
this smaller box. Its private and attached endpoint equations and
its ordinary conditional equation give
\[
 \mathcal F_e=\mathcal F_s=\mathcal F_z=0,\qquad
 \mathcal F_b=p_b
                         \quad\text{at }(e_*,s_*,z_*,b_*).
 \tag{98}
\]
These are the original zero logarithmic lifts. Subtracting the
prescribed real \(b\) tangent therefore gives \(f_x(x_*,c)=0\)
and \(f_k(x_*,c)=-\Im\mathcal F_z=0\) for the original phase.
Strict concavity identifies \(x_*\) with the unique global real
maximizer at \(c\), and proves \(G(c)=M,\ G'(c)=0\).
No claim that the forced branch has that same initial maximizer
is used.

Consequently, for an actual next-type-three reference, the remaining
new analytic premise for the common central gap at \(H_0=.01\)
is precisely the upper bound \(K_{\rm eff}\le6\pi\) along the
original phase's maximizing path on \([c,H_0]\), with the
valid active-face interpretation of Lemma 1. If that bound is
proved, both branch maxima are below \(M-1/500\) by
(72)--(76). This section does not prove that curvature inequality.
It likewise supplies no bound for a missing real tail, alias or
connecting current.
