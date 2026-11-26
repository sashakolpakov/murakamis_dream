# The right private face from its correlated incoming radius

Research deduction, 7 November 2026. The real private face \(e=.49\)
retains a strict coupled gap on the added ordinary \((3,4)\) interval.
The key comparison uses the same actual transform height in the new
face marginal and the reference marginal. It improves the former
uniform transport cost \(103/2000\) to \(7/400\).

The proof uses one already recorded family maximum from the completed
saved-only comparison. It does not change that checker, its prescribed
cost, its six-of-eight outcome, or any saved record, and performs no
new source evaluation or comparison run.

## 1. Literal face and actual reference marginal

Retain the original ordinary pair, source and actual reference from
[the face-extension theorem](research_mixed_three_four_private_left_right_extension.md):
\[
\begin{gathered}
 a_*=A+ic,\quad t_*=T+ih,\quad e_*=E+iv,\\
 .278<A<.391,\qquad .246<T<.350,\qquad -.108<h<-.020,\\
 -.072<c<.021,\qquad .333<E<.363,\qquad -.051<v<-.019 .
\end{gathered}
\tag{1}
\]
The original phase, with all its markings, is
\[
 \Phi(a;t,e)=S(e)+g(a+t)+g(e+t)-3g(t)-g(e)-g(a)
             -\frac{\pi i}{2}(e-e^2)+2\pi iat .
\tag{2}
\]
Its incoming derivative is independent of the private coordinate:
\[
                 \Phi_a=g'(a+t)-g'(a)+2\pi it .
\tag{3}
\]
In particular the actual stationary equation gives
\(p=\Re P_1'(a_*)=\Re\Phi_a(a_*;t_*,e_*)\).

Put \(b=9/20\), \(\kappa_*=1/2500000\), and
\[
 \begin{split}
 M&=\Re\{T_0(a_*)+P_1(a_*)\},\\
 B_U(x)&=\Re T_0(a_*)-p(x-A)-\kappa_*(x-A)^2,\\
 F(x,u)&=\Re\Phi(x+ic;u+ih,49/100),
                      \qquad .15\le u\le.5 .
 \end{split}
\tag{4}
\]
The whole first cap has upper rate \(B_U(x)\) on \(b\le x\le.5\).
This uses the original shared equation \(T_0'+P_1'=0\);
it is not a replacement of the terminal source by a real-row maximum.
There is no incoming \(d_N\) in this ordinary pair.

## 2. A radius comparison with the original reference

**Lemma 1.** For every \(u\) in (4) and \(b\le x<.5\),
\[
                  F_x(x,u)-p<\frac12\log2 .
\tag{5}
\]
Its integrated inequality extends to \(x=.5\), including a possible
zero of the incoming numerator.

*Proof.* Use the two actual radii
\[
 R=e^{2\pi c}>0,\qquad q=e^{-2\pi h}>0,\qquad
 D_z=|1-Re^{-2\pi iz}|.
\]
The exact derivative and original marginal are
\[
 F_x(x,u)=\log\frac{|q-Re^{-2\pi i(x+u)}|}{D_x},
 \qquad
 p=\log\frac{|q-Re^{-2\pi i(A+T)}|}{D_A}.
\tag{6}
\]
The factor \(q\) in both formulas is the same, because this
flattened private face retains the actual transform height \(h\).
Equation (6) includes the chirp in (2).

Since \(0<A<b\le x\le.5\), the cosine decreases on these real
arguments, and \(D_x\ge D_A>0\). Moreover
\[
                 .524<A+T<.741
\]
places the reference cosine strictly below zero. Therefore
\[
 |q-Re^{-2\pi i(A+T)}|>\sqrt{q^2+R^2},
 \qquad
 |q-Re^{-2\pi i(x+u)}|\le q+R
                              \le\sqrt{2}\sqrt{q^2+R^2}.
\tag{7}
\]
Dividing (6) gives (5). No independent bound or sign for \(p\)
is used.

If the new numerator vanishes, its logarithmic derivative is
interpreted on the complementary intervals. The primitive in (2)
is continuous, its real derivative is locally integrable, and the
same integrated upper inequality passes to the endpoint. This is
the original numerator corner, not a division by a finite source
zero. \(\square\)

The proof also applies with any fixed private coordinate or fixed
private penalty for which the original phase is defined. Its useful
structural hypothesis is the common transform radius and the
reference angle \(A+T\in(1/2,3/4)\). Here it is used only for the
specified \(e=.49\) face, without enlarging its geometric eligibility.

Integrating before maximizing over \(u\), and adding the complete
first-cap plane, gives
\[
\begin{split}
 B_U(x)+F(x,u)
 &\le B_U(b)+F(b,u)
       +\frac{\log2}{2}(x-b)
       -\kappa_*[(x-A)^2-(b-A)^2]\\
 &< B_U(b)+F(b,u)+\frac7{400},
                         \qquad b\le x\le1/2 .
\end{split}
\tag{8}
\]
The last inequality uses \(x-b\le1/20\), \(\log2<7/10\),
and the nonnegative square difference. For an elementary
logarithm witness, \(e^{7/10}>1+7/10+(7/10)^2/2+(7/10)^3/6>2\).
The negative quadratic change has not been reassigned to the
terminal factor.

## 3. The already recorded reserve pays this smaller analytic cost

The sole completed saved-only result is
repro/results/research-mixed-three-four-right-strip-saved-faces.json,
SHA256
abd1f98e09312ba8c6ceffcb88478a8f031730cc845f31e483e8bd143612ea14.
Its frozen checker and protocol are
[the fixed saved-face protocol](research_mixed_three_four_right_strip_saved_faces_protocol.md),
with checker SHA256
9d43648472fed4156df69b5d22a7f4664903da3cfeca462d8b0bf4d74c6ae35b.
That result retains all original reference cells and all selected
source and exclusion associations. It reports the prescribed
\(103/2000\) comparison for family 3 as inconclusive.

Independently of that cost, its field
\(\texttt{families[3].maximum\_original\_upper\_rational}\)
records
\[
                         U_3=-\frac{K}{10^{99}},
\tag{9}
\]
where
\[
 K=
 24332898998566372411239337247086503456776866875612898659443533682354590594385729320142698855914807 .
\]
The denominator has exactly 99 zeroes. The 98-digit positive
integer \(K\) begins with \(243\), so
\(K>24\cdot10^{96}\). Thus the written rational consequence is
\[
                             U_3<-\frac3{125}.
\tag{10}
\]
The witnessing original job is 318, cell 15. The family contains
1,828 source-bearing and 83 excluded-only jobs, all 1,911 jobs
with verified original coverage. Excluded-only jobs were assigned
no numerical source value. Its original displayed witness is
\[
[-0.024332898998566372411239337247086503456776866875612898659443533682354590594385729320142698855915
 \mathbin{+/-}1.93\cdot10^{-97}].
\]
Equation (9) is the saved outward upper, including that radius.

The original family-3 comparison bounds the whole free transform
interval at the actual transform height, relative to the bare
terminal plane:
\[
 F(b,u)\le
 \Re P_1(a_*)+p(b-A)-\kappa_*(b-A)^2+U_3.
\tag{11}
\]
The record covers more reference cells than this theorem requires;
the transport argument still uses only the actual ordinary
\((3,4)\) references (1). No new filter or changed eligibility is
introduced.

Adding (11) to \(B_U(b)\), then using (8)--(10), yields
\[
\begin{split}
 B_U(x)+F(x,u)
 &<M-\frac3{125}+\frac7{400}
               -2\kappa_*(b-A)^2\\
 &\le M-\frac{13}{2000},
                 \qquad b\le x\le1/2,\quad .15\le u\le.5 .
\end{split}
\tag{12}
\]
This is a written corollary of the immutable recorded maximum and
the new analytic lemma. No second checker run, altered saved cost,
source replay, or new numerical evaluation is involved. The
original six-of-eight status remains unchanged.

## 4. Finite face currents and original color scope

The finite source underlying (2) is the same retained row as in
the prior extension:
\[
 \widehat{\mathcal J}_N(a,t,e,w)=
 e^{2\pi iNat}\Pi_N(a+t)\Pi_N(e+t)
 E_N(a)E_N(t)^3E_N(e)\Delta_N(e)^{-1}\mathcal C_N(e,w).
\tag{13}
\]
Here \(\mathcal C_N\) is the complete original ordinary endpoint
coefficient. The \(e=.49\) face has \(t=u+ih\), with the original
inner half-grid endpoints and the original residue coefficients.
Every reciprocal factor is regular there. At a possible
\(a+t=1\) numerator zero, use exactly the zero-safe quarter-level
shift from Section 5 of the prior extension. It supplies a uniform
upper rate through the zero and the rounded cut; no numerator is
divided out.

Equation (12), the complete first-cap upper bound, and (13)
therefore give
\[
  |U_{0,N}(w_L,e^{-2\pi i(x+ic)})|\,
       |\mathcal I_N^{e_R}(w_R,x+ic)|
       \le C N^B e^{N(M-1/200)} .
\tag{14}
\]
This includes every fixed ordinary-color derivative, on smaller
fixed disks, and both level parities. It also supplies the same
rate as an anchor in the original private-tail or vertical-
convexity reductions. All original polynomial prefactors and
residue powers remain in \(\mathcal I_N^{e_R}\).

To justify the finite weakening, the difference between
\(13/2000\) and \(1/200\) is \(3/2000\). Allocate a smaller
total tolerance among the complete endpoint packet, the complete
first cap, the numerator-wall upper bound and the color
neighborhoods. Half-grid rounding costs \(O(\log N/N)\), and
all fixed derivatives follow by Cauchy's formula. The exact
ordinary one-circle scalar \(\kappa_N^3N^2\) is unchanged.

Other endpoints of any vertical current remain separately
required. In particular this theorem does not pay the real
transform-left face \(t=.15\), change the incoming height,
bound the far half-circle, or establish the entire ordinary
two-boundary source.

