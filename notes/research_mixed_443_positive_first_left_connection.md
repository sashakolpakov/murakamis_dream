# Connecting the early first contour when the second variable is real

Private written proof, 11 November 2026. This note continues the
positive first contour down to the real axis and then to zero, while
the second coordinate remains on \([1/2,18/25]\). The upper sampling
height is kept finite. Its new zero-face comparison includes the cap
and uses an integrated horizontal gain to pay for changing height.

Author-frozen after full proof and direct-source readback; not yet
adopted. The early selected horizontal input has completed its
separate review. This note requires its own separate full review
before adoption. All public and previously frozen files are unchanged.

## 1. Statement and fixed source

Use the actual \(4,4,3\) reference, finite functions, normalized
factorial, phases and number \(\delta>0\) of
[the early selected horizontal proof](research_mixed_443_selected_early_first_right_pair.md).
In particular \(H=1/100\), \(h_U=\log2/(4\pi)\),
\(q\in[1/2,18/25]\), \(z=b+ic_3\), \(b\in[11/50,9/20]\),
and all reference heights remain fixed.

For \(X=e^{-2\pi ia}\), \(Y=e^{-2\pi iq}\), \(Z=e^{-2\pi iz}\),
write the original complete product as
\[
 \mathcal J_{\nu,\mu,N}(w;a,q,z)
 =U_{1,N}(w,X)d_N(X)X^{-\nu N}C_{1,N}(X,Y)
                    d_N(Y)Y^{-\mu N}C_{0,N}(Y,Z).             \tag{1}
\]
The second choice \(\mu\) is either zero or one throughout.
There is no outgoing halfweight.
Here \(U_{1,N}\) is the original cap polynomial, \(C_{1,N}\)
and \(C_{0,N}\) are the complete conditional sums in equation
(3) of the linked source, and \(d_N\) is the degree-\((N-1)\)
interpolation polynomial for the reciprocal factorial values.
The symbols \(\Psi,Q_1,g,\Lambda_{123}\) retain precisely that
source's phases, logarithmic marking and calibrated affine rate.
Write \(J(t)=\Re g(t)\) on the real axis, extended periodically,
and \(G_h(t)=\Re g(t-ih)\) for \(h\ge0\). In particular
\(G_0=J\). All real logarithmic zeros below are interpreted by
their integrable limits.

**Theorem.** Uniformly on the connected first path
\[
                 0\longrightarrow1/10
                 \longrightarrow1/10+iH
                 \longrightarrow11/50+iH,                  \tag{2}
\]
the complete product has a bound
\[
 |\mathcal J_{\nu,\mu,N}|
       \le CN^A e^{N\{\Lambda_{123}(z)-\delta/32\}}.            \tag{3}
\]
On the nonreal pieces take \(\nu=1\). On the real piece both
\(\nu=0,1\) are included. The statement holds at both parities,
on a sufficiently small fixed ordinary-color disk about \(-2\),
and for fixed derivatives on smaller disks. Each integral retains
the original density \(+N\,da\) and its chosen orientation.

The first negative-height horizontal and its join are not covered.
Neither are the real first arcs after \(1/2\) or the later second
interval. This is not a complete first or second summation theorem.

## 2. The comparison at the real first face

Keep the same cap profiles \(A_0,A_L,A_R,A_-,A_+\) and true-end
ceiling as the early horizontal proof. Their complete finite-source
bound on the height interval used here is
[the independent-height cap theorem](research_mixed_cap_early_fixed_height_full_source.md),
Theorem 2, with its own flag equal to one. Each regular cap point has
\[
 e=u+i\xi,\qquad .27\le u\le.49,\quad -.055\le\xi\le.04,
\]
with its original sampling penalty. Put \(x_-=1/10\),
\(x_+=11/50\), \(a_+=x_++iH\).

The primary first profiles are the actual negative horizontal at
\(h_2\), the lower correction at \(-1/5\), the upper correction
at \(h_U\), and the real left and half profiles.
The upper rate retains its period multiplier exactly, as in
Section 3 of the early horizontal proof. Every term in that
multiplier is independent of \(a\).

For a fixed private first point \(s=t+i\eta\), exact
differentiation at incoming height zero gives
\[
 \partial_x\{\Re\Psi(e,x)+\Re Q_1(s;x,q)-J(x)\}
                 =\log\frac{N_e(x)N_s(x)}{D(x)^3},            \tag{4}
\]
where
\[
 N_e=|1-e^{2\pi\xi-2\pi i(u+x)}|,\quad
 N_s=|e^{-2\pi\eta}-e^{-2\pi i(t+x)}|,\quad
 D=2\sin\pi x,\quad J(x)=\Re g(x).
\]
All penalties and all factors depending only on \(q,z\) are fixed
in this differentiation, also after a numerator crosses a period.

For \(\eta\le0\), the proof of Sections 3--5 of
[the old zero-height face](research_mixed_selected_four_four_zero_height_face.md)
applies pointwise. Its horizontal argument uses only
\(e^{-2\pi\eta}\ge1\), \(1/8\le t\le1/2\), and the displayed
cap rectangle. Its height-reset argument uses all-radius argument
bounds. Thus it also covers the present lower correction at
\(-1/5\), and a real half profile with its second argument \(1/2\).
It proves an integrated horizontal gain greater than \(7/100\)
and a reset cost at most \(109\pi/5000\). The difference is
greater than \(1/2000\). For the true cap end the corresponding
gain is greater than \(3/100\) and cost at most \(11\pi/2500\).
These comparisons do not use the original second-coordinate domain:
the differentiated expression is (4), independent of that coordinate.

The positive upper private height needs a different horizontal bound.
Its maximum may be restricted to \(1/8\le t\le2/5\), uniformly
for incoming heights between zero and \(H\). The force argument in
the early horizontal proof still holds: \(e^{-2\pi\Im a}\le1\),
so on \(2/5\le t\le1/2\) its squared force is less than \(3/20\).

For this upper line let \(p=e^{-2\pi h_U}=1/\sqrt2\).
The cap bound from the old zero-face proof is
\[
                         N_e^2>9/5.                         \tag{5}
\]
For \(x\in[1/10,4/25]\), the shifted ordinary cosine is less
than \(1/6\), giving
\[
                         N_s^2>5/4.
\]
For \(x\in[4/25,11/50]\) it is less than \(-1/5\), giving
\[
                         N_s^2>7/4.                         \tag{6}
\]
Indeed \(t+x\) lies in \([.225,.62]\); on the second subinterval
its lower endpoint is \(.285\). The cosine witnesses are precisely
those in Section 3 of
[the selected early source](research_mixed_selected_four_four_early_complete_source.md),
and
\(N_s^2=3/2-\sqrt2\cos2\pi(t+x)\).

The concavity of \(\log(2\sin\pi x)\) gives the same mean bound
as in the old zero-face proof:
\[
 \frac1{x_+-x_-}\int_{x_-}^{x_+}\log D(x)\,dx
           \le\log(2\sin(4\pi/25))<\log(49/50).
\]
Both subintervals in (6) have length \(3/50\). Integrating (4)
therefore gives
\[
 \text{horizontal gain}>
       \frac3{100}\log(567/80)+\frac9{25}\log(50/49)
                                      >\frac{13}{200}.       \tag{7}
\]
Here is a rational witness for the last step.
The exponential series gives
\[
 e<65/24+1/100=1631/600<68/25.
\]
The tail after degree four is bounded by
\((1/120)\sum_{j\ge0}6^{-j}=1/100\).
Consequently
\[
 \log7>2-\frac{249}{4375}>\frac{29}{15},
\]
by \(\log(1+v)<v\). Since \(567/80>7\) and
\(\log(50/49)>1/50\), the right side of (7) is greater than
\(29/500+9/1250=163/2500>13/200\).

At \(x=x_+\), write
\(\mathcal A(v,h)=\Arg(1-e^{2\pi h-2\pi iv})\) with the
original marking. For \(0\le h\le H\),
\[
 \mathcal A(x_+,h)\ge7\pi/25,\qquad
 \mathcal A(u+x_+,\xi+h)\le\pi/50.
\]
Because \(t\le2/5\),
\[
 \mathcal A(t+x_+,h_U+h)+2\pi t\le4\pi/5.
\]
For a shifted real part below \(1/2\), the left side is at most
\(14\pi/25\); above it the argument is nonpositive.
It follows that the derivative in incoming height of the full
regular joint rate, including the selected monomial, is at least
\[
              3(7\pi/25)-\pi/50-4\pi/5-2\pi
                                      =-99\pi/50.
\]
Thus the upper-line reset costs at most \(99\pi/5000\).
Together with (7), this leaves more than
\[
                    13/200-99\pi/5000>1/500.                 \tag{8}
\]

For a true cap end the horizontal derivative is
\(\log(N_s/D^2)\). Equation (6) gives a gain greater than
\[
 \frac3{100}\log(35/16)+\frac6{25}\log(50/49)
          >\frac1{50}+\frac6{1250}.
\]
For the first term, \(\log(35/16)>38/51>2/3\) follows
from \(\log t>2(t-1)/(t+1)\) for \(t>1\).
The affine \(2\pi h\) in its actual endpoint ceiling cancels
the selected monomial. Its reset derivative is bounded below by
\(2(7\pi/25)-4\pi/5=-6\pi/25\), hence the cost is at most
\(6\pi/2500\). The gain exceeds this cost by more than \(1/100\).

Take maxima only after these pointwise comparisons. At the anchor
\(a_+\), the complete pair proof supplies the paid negative
and upper horizontal profiles with every cap and complete-third
profile. Its first half-index comparison also retains \(1/30\)
of extra margin. Equations (4)--(8) therefore pay the same primary
profiles at the real face \(a=x_-\), with positive extra margins.
No estimate of a cancelling modulus is used to infer a profile bound.

## 3. Completing the real face

The early horizontal proof's first private left-cut curvature applies
also at \(a=x_-\): replacing \(H\) by zero improves its radius
bound. The first private right-cut argument uses only
\(0<x\le1/2\), so it applies as well. Every zero-mode join and
weighted vertical half is therefore bounded by the primary
endpoints already paid in Section 2, with a fixed arbitrarily small
right-cut allowance.

The first low physical rows increase to their real cut; the proof
in Section 5 of the early horizontal note is valid at incoming
height zero. Its first high-row estimate also remains valid:
at \(x=1/10\), \(0\le h\le H\), and real \(q\),
\[
 E_2(t;1/10+ih,q)
       \le\max\{E_2(1/2;1/10+ih,1/2),\,0\},
                 \qquad 1/2\le t\le1.                       \tag{9}
\]
The same reflection proof uses \(G_h\) in place of \(G_H\);
its short-interval argument has \(v\le1/10=x\), and its other
argument uses the unchanged leg and chord inequalities.
The drift is still zero.

The first half carrier at the real face retains the anchor's
\(1/30\) margin by the nonpositive-private-height transport
in Section 2. It pays the complete third kernel's possible
increase \(1/4240\).
For the first last carrier zero, the real half-face left rate
satisfies \(E_2(1/8;1/10,1/2)>3/8\), by the scalar proof in
the early horizontal note (the incoming chirp loss is now zero).
Use the transported left-cut calibration and spend this reserve
on the same possible third increase.

The exact first finite contour has heights \(-1/5,h_2,h_U\),
cuts \(1/8,r_0\), both joins and all four weighted halves.
The shifted \(q\) numerator uses its original period multiplier
and the uniform wall upper estimate of the complete pair proof.
No denominator leaves its regular strip. The third finite source
is exactly the paired-upper theorem's complete source on
\([1/2,18/25]\). Thus Section 2 bounds every part of the complete
product at the real face, for both first monomials, which have
unit modulus there. It supplies a common raw envelope with a
margin greater than \(\delta\), before fixed source allowances.

## 4. The positive vertical segment

Use one common first-source envelope for
\(a=1/10+ih,\ 0\le h\le H\). It retains the six cap alternatives,
every first central current and its original penalty, the first
real left cut, the half carrier in (9), and the last carrier zero.
Use identical fixed private cuts and heights at both endpoints.
The third source and second weight are independent of \(h\).

Every regular cap and first contour profile is convex in \(h\).
The proof in Section 4 of
[the positive-join envelope](research_mixed_first_positive_join_convex_envelope.md)
uses
\[
 \Re\cot\pi(1/10+ih)>25/9,\qquad
 \Re\cot\pi(t+i\eta)\le3/2\quad(1/5\le t<1).
\]
Our first shifted real parts lie in \([.225,.6]\), and the cap
ones in \([.37,.59]\). Hence
\[
\begin{split}
 \partial_h^2\Re\Psi(e,a)
    &=\pi\{\Re\cot\pi a-\Re\cot\pi(e+a)\}>0,\\
 \partial_h^2\Re Q_1(s;a,q)
    &=\pi\{\Re\cot\pi a-\Re\cot\pi(s+a)\}>0.
\end{split}                                                    \tag{10}
\]
These derivatives are independent of \(q\). Its numerator-wall
multiplier is independent of \(h\) as well. The same identities
apply to all retained private joining points, not only horizontals.

The true cap-end rate is affine. The half carrier in (9) has
second derivative
\(\pi\{\Re\cot\pi a-\Re\cot\pi(a+1/2)\}>0\);
the last carrier is constant. The full selected first-weight
rate \(\max\{-\Re g(a)-2\pi h,0\}\) is convex.
Consequently the maximum of these complete profile sums is convex.

This envelope is a bound for the full source for every height.
The independent-height cap estimate applies; the first low rows
retain their increasing-ratio bound; (9) covers every high row.
Every central current is explicitly retained, with the same
finite recurrence through the \(q\) wall.
At \(h=0\) the envelope is paid by Section 3, and at \(h=H\)
by the early horizontal proof, at the profile level.
Convexity pays the entire vertical. This is not an assertion
that the modulus of the finite sum is convex.

## 5. The real interval down to zero

Fix \(0<\rho<1/10\) before \(N\).
On \(\rho\le a=x\le1/10\), the cap-only construction in Section 2
of [the real first-interval proof](research_mixed_four_four_real_first_interval.md)
applies unchanged: it depends only on the first coordinate.
It supplies the same five private cap profiles and the true-end
ceiling \(3/5+\log4/100\), including the near-last physical rows
whose omitted numerator arc can contain a zero.

For each fixed cap and first private point, including every
horizontal and vertical sampling point, differentiation gives
(4). On this real first interval,
\[
               N_e>1,\qquad N_s\ge1/\sqrt2>7/10,\qquad D<5/8.
\]
These are the all-radius inequalities in Section 4 of that
real-interval proof, using shifted real intervals
\((.27,.59]\) and \((1/8,.6]\).
They are independent of the outgoing coordinate and are valid
for the new finite upper height and its period multiplier.
The regular derivative in (4) exceeds \(1/3\); the true-end
derivative \(\log(N_s/D^2)\) also exceeds \(1/3\).
Thus the complete central-current envelope decreases toward zero,
with gain at least \((1/10-x)/3\).

The physical groups require checking rather than importing the old
outgoing-angle statement. For \(t\le1/8\), the first incoming
modulus is at least its own sine modulus, because \(t+x\le.225\).
The outgoing modulus exceeds \(4/5\), while the own squared modulus
is below \(16/25\). The first low rate therefore increases to the
left cut.

For high rows, retain the reflected formula (19) of the early
horizontal proof at height zero. If \(v\le1/10\), the minimum
integral of the even, one-periodic function \(G_0'\) over an arc
of length \(v\) occurs on the arc centered at zero. Therefore
\[
 G_0(x-v)-G_0(x)\le-2J(v/2).
\]
The remaining terms give
\(3J(v)-2J(v/2)-v\log(3/2)<0\), since \(J\) decreases on
\([0,1/10]\). The centered-arc statement also follows directly
by differentiating the integral with respect to its center; the
integrand increases with distance to its nearest integer.
For \(v\ge1/10\) the all-angle leg and the same \(F_{1-q}\)
chord again give the half carrier. Hence (9)'s half/last reduction
holds for every \(0<x\le1/10\).

The half carrier is a real private point \(s=1/2\), with second
argument fixed at \(1/2\). The same derivative transport compares it
with its paid value at \(x=1/10\).
For the last carrier zero, the regular cap-plus-first-weight
derivative is \(\log(N_e/D^2)>1/3\); for the true cap end it is
\(-\log D>1/3\). Thus both high carriers transport with a gain as
well. All third profiles are constant during this first-coordinate
motion.

Use the complete finite contour with the same fixed heights and
cuts, retaining every joining point before this transport. The
\(q\) numerator wall is handled by the original recurrence; its
denominators stay regular. The finite-product proof in Section 2 of
[the contour-allowance note](research_mixed_conditional_contour_allowance.md)
gives all physical-row estimates with an arbitrary allowance,
including at a numerator zero. Both first
monomials have unit modulus. We obtain a bound with the real-face
margin and the additional gain \((1/10-x)/3\), uniform on each
fixed interval \([\rho,1/10]\).

Finally, for either \(\nu\), the complete expression (1) has
Laurent support in \(X\) contained in
\[
                  [-(1+\nu)N+1,\ (2-\nu)N-2].
\]
The third factor and second weight are constant multipliers in
\(X\), including when they vanish. Lemma 1 of
[the real-endpoint continuation](research_mixed_four_four_real_first_endpoint.md)
therefore extends the bound to zero with arbitrarily small fixed
exponential cost. Choose that cost and its fixed starting interval
before \(N\). No factorial asymptotic is used at \(X=1\), and
no finite source factor is divided out.

## 6. Margins, colors and scope

All first and third finite currents, their literal densities,
physical rows and exact Fourier polynomials have been retained.
The common raw margins at the calibrated endpoints exceed
\(\delta\); the new upper reset in (8) and the existing negative
reset have positive additional reserves. The vertical interpolation
and real first transport spend none of those margins.
Choose fixed collars, the endpoint-continuation cost, the source
allowances and ordinary-color continuation with total cost less
than a fixed fraction of the available margin. In particular (3)
follows with gap \(\delta/32\).

The cap bounds hold for all real ordinary colors; every other
factor is color-independent. The exact degree in that color is
less than \(N\). The same interval polynomial continuation as in
the source proofs supplies fixed small disks at arbitrarily small
exponential cost; Cauchy's formula supplies fixed derivatives.
All choices precede \(N\), and both parities are included.

The finite-exception goal still needs the missing first paths,
the remaining second interval, and a composition theorem valid
for arbitrary short partial fillings. This connected positive
first contour is one input to that work.

## Direct source versions

The zero-face source is used for its pointwise horizontal and
height-reset inequalities, not for its old outgoing-parameter
theorem. The positive-join source supplies the cotangent inequalities
and convexity argument. The real-interval source supplies its
complete cap construction and pointwise first-coordinate derivatives.
The endpoint source supplies its general Laurent-polynomial lemma.
The high-row source supplies only its disk primitive and leg
inequality; the reflected estimates for the new second interval
are proved here. The two complete-pair sources supply the original
calibrations, third-factor bounds and finite continuation across
the second numerator wall.

| Direct source | SHA-256 |
|---|---|
| research_mixed_443_selected_early_first_right_pair.md | b1fc75fbcedabd116ed61ade612a50f8c284673c6931fca34153dea8c7594c89 |
| research_mixed_443_core_first_complete_right_pair.md | 3f3fa659048dd5961e54a29d71bdcd6e6b73bd4927e4d802ffa8e0849b86cd21 |
| research_mixed_443_paired_upper_prewall_currents.md | 9b851f2e88f14be3116be661d8377bae514c77c28fbe594011b5966acc4ea77e |
| research_mixed_selected_four_four_zero_height_face.md | fe99fcefe1618991471f083febcf4c6043418a4387d76be1ae2015542734810f |
| research_mixed_selected_four_four_early_complete_source.md | 760ab93cc36ccba00eea97c518eb3697f55638b90c43c90d5ce1a9cd029ddc05 |
| research_mixed_first_positive_join_convex_envelope.md | b1f18bb5a79ff958654190c960c933ac7839f1da3fc86635f6222a1ea58cb774 |
| research_mixed_four_four_real_first_interval.md | b848eb005f99d57259662ef3a864b207e093b6ebfaf4c34c2dbcc1e9727d58fc |
| research_mixed_four_four_real_first_endpoint.md | 4ceec7f835d08ef971b3b3ccadcf7eecd74e48db3d422cbd09e5611c0572c122 |
| research_mixed_all_angle_high_row_sign_class.md | 3a959f0a6bb064767e753e90061a2d9ef323268e79cbdf19c1043a6fe9691144 |
| research_mixed_conditional_contour_allowance.md | 12b80f46ea2778c3617fc39099a321592605f07677b9a424ba3153851d037f70 |
| research_mixed_cap_early_fixed_height_full_source.md | d930407eaa5a0bb7c735ee9521c6d352f637124c57c5593cbb1813f069f7d423 |

The author read the full final proof and all eleven directly used
source implications, and checked all eleven source hashes.
This is a written proof; no mathematical numerical evaluation,
test, import, compilation or edit to a frozen source was used.
