# Paying the ordinary last rows next to a selected first cap

Research deduction, 6 November 2026. For an actual first-four/next-three
reference, all five cap profiles paired with the ordinary last-row
profile have a strict selected gap. The argument retains the actual
negative incoming reference height, both Fourier alternatives, and the
original outgoing affine term. It reduces the nineteen outstanding
profiles of the finite-source reduction to fourteen.

It also gives a bound for a literal finite sector: the whole first cap
times all ordinary rows with index at least \(39N/50\) has gap \(1/40\).
The remaining ordinary rows and fourteen boundary profiles are not
settled here. No source calculation, root solve, or numerical cover is
used.

## 1. Source, profiles and the original negative-height comparisons

Use the exact source and notation of
[the finite first-four/next-three reduction](research_mixed_selected_four_three_finite_reduction.md).
In particular
\[
 H=7/625,\quad z_H=y+iH,\quad z_c=y+ic,\quad
 y,v\in[.22,.45],\quad b=v+ih_b,\quad
 -.07<c<-.02,\quad -.065<h_b<.068.
\tag{1}
\]
All reference data come from the same actual open critical point of a
word of length at least three beginning with types four and three.
The cap private contour is
\[
 E=[.27,.49]+i[-.055,.04],
\qquad
 \Psi(e,z)=S(e)+J(e+z)-J(z)-i\pi ez-g(e).
\tag{2}
\]
Let \(A_i^k(y)\), \(i\in\{0,L,R,-,+\}\), be the five cap
profiles in equation (6) of that reduction, with outgoing height \(k\).
The main private height remains the original \(h_e\); both real cuts
and both alias heights and penalties are unchanged when \(k\) varies.
Write \(G_c(y)=\Re g(y+ic)\). The bare full last-row rate is
\[
 B_1^k(v)=2\pi(-k)_++2\pi(h_b)_+.
\tag{3}
\]
The notation \(B_1^H=B_1\) agrees with the selected finite reduction.

Set \(\kappa=1/2500000\), \(d_y=y-\Re z_*\),
\(d_v=v-\Re b_*\). Retain its calibrated joint action \(M\)
and original outgoing term \(\ell_b(v)=\Re p\,d_v\).
The already proved negative-height comparisons imply, for every cap
profile separately,
\[
 A_i^c(y)+B_1^c(v)-G_c(y)
 \le M+\ell_b(v)-2\kappa d_y^2-\kappa d_v^2.
\tag{4}
\]

Here is the precise source of (4). The completed
[first-cap supporting-plane proof](research_mixed_first_cap_plateau_completion.md)
has the main-line inequality and each of its four cut/alias
inequalities
\[
 A_i^c(y)-\tfrac12G_c(y)\le
 \Re L_{\rm cap}+\Re p_{\rm cap}\,d_y-\kappa d_y^2.
\tag{5}
\]
We use those individual current inequalities, not an inference from
the modulus of a cancelling whole cap. The completed
[ordinary last-row comparison](research_mixed_three_row_source_assembly.md)
gives
\[
 B_1^c(v)-\tfrac12G_c(y)\le
 \Re L_{\rm ord}+\Re p_{\rm ord,a}\,d_y+
 \Re p_{\rm ord,b}\,d_v-\kappa(d_y^2+d_v^2).
\tag{6}
\]
Both comparisons apply to every actual reference under discussion,
including the ordinary middle vertex of a length-three word with two
attached external inputs. There is no outgoing Fourier halfweight
at the own-three coordinate \(b\).
The original unexponentiated equation gives
\(p_{\rm cap}+p_{\rm ord,a}=0\);
also \(L_{\rm cap}+L_{\rm ord}\) has real part \(M\) and
\(p_{\rm ord,b}=p\). Adding (5)--(6) proves (4).
Thus the actual shared tangent cancels once, while the outgoing
tangent remains. No selected-height source estimate has been imported
into (4).

## 2. Uniform cap transport at every original private contour point

Put
\[
 A(t,h)=\arg(1-e^{2\pi h-2\pi it}),\qquad 0<t<1,
\tag{7}
\]
on the original regular-strip lift. The elementary radius bounds are
\[
 \pi\min(1-2t,0)\le A(t,h)\le\pi\max(1-2t,0).
\tag{8}
\]
For \(0<t<1/2\), the stronger negative-height bound is
\[
 0<A(t,k)\le\pi(1/2-t),\qquad k\le0.
\tag{9}
\]
Indeed its positive argument increases with its radius and at radius
one is \(\pi(1/2-t)\). These are precisely the original argument
bounds used in the fixed-current transport proofs.

Fix any \(e=x+i\eta\in E\), and let
\(\Phi_e(k)=\Re\Psi(e,y+ik)\), \(G(k)=\Re g(y+ik)\).
The exact marginal, with the cap chirp included, gives
\[
 \Phi_e'(k)=A(y,k)-A(x+y,\eta+k),\qquad
 G'(k)=-A(y,k).
\tag{10}
\]
All arguments are regular throughout \(c\le k\le H\):
\(.22\le y\le.45\) and \(.49\le x+y\le.94\).
In particular (10) is valid for real cuts, both aliases, the main
private line, and all their joining points.

**Lemma 1.** On these whole domains,
\[
\begin{array}{c|c|c}
 &c\le k\le0&0\le k\le H\\ \hline
 \Phi_e'(k)&\le93\pi/100&\le49\pi/50\\
 (\Phi_e-G)'(k)&\le49\pi/50&\le77\pi/50 .
\end{array}
\tag{11}
\]

*Proof.* If \(x+y\ge1/2\), (8)--(9) give, on the negative
path,
\[
 \begin{split}
 \Phi_e'&\le\pi(1/2-y)+\pi(2x+2y-1)
                  =\pi(2x+y-1/2)\le93\pi/100,\\
 (\Phi_e-G)'&\le2\pi(1/2-y)+\pi(2x+2y-1)
                  =2\pi x\le49\pi/50.
 \end{split}
\tag{12}
\]
On the positive path use \(A(y,k)\le\pi(1-2y)\). The
corresponding two upper bounds are
\(2\pi x\le49\pi/50\) and
\(\pi(1+2x-2y)\le77\pi/50\).
If \(x+y<1/2\), its argument is nonnegative and may be
dropped with a favorable sign in (10). The four resulting bounds
are respectively \(7\pi/25,14\pi/25,14\pi/25,28\pi/25\),
all smaller than their entries in (11). At equality of the summed
real part with one half that argument is zero. This proves every
case. \(\square\)

## 3. Both full Fourier alternatives pay the last-row loss

Use the complete selected rates
\[
 W_{\rm fac}(y)=-G(H)-2\pi H,\qquad
 W_{\rm force}(y)=0,
\tag{13}
\]
and retain the original unselected full rate \(-G_c(y)\).
The two halves from (5)--(6) have already combined into this full
weight. The endpoint-forcing alternative of the actual \(d_N\)
is not dropped.

**Proposition 2.** Every one of the five cap profiles satisfies,
for both alternatives,
\[
 A_i^H(y)+B_1^H(v)+W_\sigma(y)
 <M+\ell_b(v)-2\kappa d_y^2-\kappa d_v^2-\frac3{100}.
\tag{14}
\]

*Proof.* First consider a fixed private point \(e\); its alias
penalty, if any, is constant in \(k\). The factorial expression
is continuous through height zero when it is written as
\(\Phi_e-G\) on the negative path and
\(\Phi_e-G-2\pi k\) on the positive path. Equation (11)
therefore gives
\[
 \Phi_e(H)-G(H)-2\pi H-\{\Phi_e(c)-G_c\}
 \le\frac{49\pi}{50}(-c)-\frac{23\pi}{50}H.
\tag{15}
\]
The ordinary last-row rate drops by the exact amount
\[
                         B_1^H-B_1^c=-2\pi(-c).
\tag{16}
\]
Their combined change is at most
\[
 -\frac{51\pi}{50}(-c)-\frac{23\pi}{50}H
 <-\frac{3194\pi}{125000}.
\tag{17}
\]

For the forced alternative, the first row of (11) instead gives
\[
 \Phi_e(H)-\Phi_e(c)
 \le\frac{93\pi}{100}(-c)+\frac{49\pi}{50}H.
\tag{18}
\]
Since \(c<0\) and \(0<y<1/2\), the original radial primitive
satisfies \(G_c(y)<0\). Relative to the baseline
\(\Phi_e(c)-G_c+B_1^c\), (16)--(18) thus give the strict bound
\[
 -\frac{107\pi}{100}(-c)+\frac{49\pi}{50}H+G_c(y)
 <-\frac{1303\pi}{125000}<-\frac3{100}.
\tag{19}
\]
The first comparison uses \(-c>1/50\) and \(H=7/625\);
the last follows already from \(\pi>3\), since
\(3909/125000>3/100\). Equation (17) gives a larger loss.
The pointwise bounds are uniform in each cap profile's private
coordinate. Taking its maximum, retaining its alias penalty, and
then applying (4) proves (14). \(\square\)

## 4. A literal finite tail sector and the reduced list

Let the following be an actual restriction of the finite conditional
sum, retaining all its original factors:
\[
 C_{0,N}^{\rm end}(X,Y)=
 \sum_{j=\lceil39N/50\rceil}^{N-1}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^2}.
\tag{20}
\]
It is paired with the whole \(U_{1,N}\), with no truncation of
its coherent endpoint coefficient.

For every \(t\in[.78,1]\), one has
\(1-t\le.22\le\min(y,v)\). The first reflection comparison
in Section 2 of the
[right-row endpoint theorem](research_mixed_right_tail_endpoint_bound.md)
therefore gives \(E(t;z_H,b)\le E(1;z_H,b)=B_1^H(v)\).
This statement includes wrapped rows and the integrable-zero
limits. The zero-safe finite product estimate then bounds every
term of (20), and their sum, by the rate \(B_1^H+\tau\).

Combine this with the cap's five-profile upper bound, the actual
Fourier polynomial upper bound, and (14). With one total tolerance
smaller than \(1/200\), both parities satisfy
\[
 \left|\partial_w^k\{
 U_{1,N}(w,X)\,C_{0,N}^{\rm end}(X,Y)d_N(X)X^{-N}\}\right|
 \le C_kN^{D_k}
 e^{N\{M+\ell_b(v)-2\kappa d_y^2-\kappa d_v^2-1/40\}}.
\tag{21}
\]
The estimate holds on a sufficiently small fixed ordinary-color disk,
for every fixed ordinary-color derivative. The complete cap packet
and full-row bounds provide the color neighborhood; the conditional
factor and Fourier weight do not depend on \(w\).

More generally, (14) removes all five \(B_1\) entries from the
profile maximum of the finite reduction. Define
\[
 \mathcal D_{14}(y,v)=
 \max_{\substack{i\in\{0,L,R,-,+\},\ j\in\{0,L,R\}\\
                           (i,j)\ne(0,0)}}
 \max_\sigma
 \{A_i^H(y)+B_j(y,v)+W_\sigma(y)-M-\ell_b(v)\}.
\tag{22}
\]
Here \(B_0,B_L,B_R\) are exactly the profiles of that reduction.
Its proved whole-source upper bound sharpens to
\[
 |\partial_w^k\mathcal K_N(w;X,Y)|
 \le C_{\tau,k}N^{D_{\tau,k}}
 e^{N\{M+\ell_b(v)+\max(-1/500,\mathcal D_{14}(y,v))+\tau\}}.
\tag{23}
\]
There are now fourteen unresolved pairs per Fourier alternative:
two ordinary cuts paired with the cap main line; two cap cuts paired
with the three ordinary profiles; and two cap aliases paired with
those three profiles. No sign for these remaining pairs follows from
(14). Their comparison still retains the common reference and the
same outgoing tangent. The result is a selected boundary-sector
bound, not whole open-word dominance or a new filling theorem.

## 5. The same last-row gap for either next type

The transport argument has a wider scope than the central comparison.
Let the first two types be \(4,3+\epsilon\), where
\(\epsilon\in\{0,1\}\), and \(m\ge3\). Keep their actual coupled
reference and allow
\[
 0\le H\le7/625,\qquad -.108<c<-.020.
\tag{24}
\]
Only the original attached-height enclosure is used here; the improved
lower bound \(c>-.07\) for a next-three vertex is unnecessary.
The outgoing coordinate remains at its actual height \(h_b\),
which is negative when \(\epsilon=1\).
Define \(M_\epsilon,p_\epsilon,\ell_{\epsilon,b}\) using the
original joint allocation with the unchanged outgoing halfweight
\(-\epsilon g(b)/2\). Its last-row profile is
\[
 \widetilde B_{1,\epsilon}^k(v)=
 2\pi(-k)_++2\pi(h_b)_+
                    -\frac{\epsilon}{2}\Re g(v+ih_b).
\tag{25}
\]

**Corollary 4.** For both next types, all five cap profiles satisfy
\[
 A_i^H(y)+\widetilde B_{1,\epsilon}^H(v)+W_\sigma(y)
 <M_\epsilon+\ell_{\epsilon,b}(v)
              -2\kappa d_y^2-\kappa d_v^2-\frac3{100}.
\tag{26}
\]
The next-four outgoing halfweight in (25) is kept on both sides of
the height comparison. This corollary does not use a next-four
central estimate.

*Proof.* The actual individual cap-current comparisons and the
completed ordinary last-row comparison apply for either own type.
Their original allocations give exactly (4), with
\(\widetilde B_{1,\epsilon}\), \(M_\epsilon\) and
\(\ell_{\epsilon,b}\) in place of the corresponding next-three
quantities. In particular the outgoing halfweight is not removed
when adding the two planes. The original shared tangent still cancels.

All bounds in Lemma 1 hold for every negative \(c\) in the original
regular strip: the estimates depend on its sign, not on a lower
bound for its value. The outgoing term in (25) is constant in the
incoming height, and \(J(1)=0\), so (16) is unchanged.
The factorial loss is at least
\((51\pi/50)(-c)+(23\pi/50)H>51\pi/2500>3/100\).
The forced loss is greater than
\((107\pi/100)(-c)-(49\pi/50)H\), whose infimum on (24)
is \(1303\pi/125000>3/100\). This proves (26), including
the endpoint \(H=0\). \(\square\)

The literal finite tail consequence also extends. Replace (20) by
the same high-index sum with denominator \(P_j^{2+\epsilon}\).
Its real-row rate differs from the own-three rate by
\(-\epsilon J(t)\). On \([.78,1]\), \(J(t)\ge0\), while
\(J(1)=0\). The same reflection comparison therefore bounds
these rows by their allocated last-row rate (25).

For completeness the cap's five-profile bound also remains valid
throughout (24), with a single arbitrary rate tolerance. Its
positive-height tail estimates and the literal ceilings \(1/4,3/4\)
are unchanged. To see that the main profile still pays those ceilings,
repeat (11)--(13) of the finite reduction at the original fixed
private \(e_*\). Now the summed height has modulus below \(.159\)
and the outgoing height has modulus below \(.108\). The elementary
bounds
\[
 \cosh(.159\pi)<8/7,\quad \cosh(.108\pi)<16/15,\quad
 \log(15/32)>-4/5,\quad \log(16/7)<17/20
\tag{27}
\]
give \(|\Re\Psi_z|<1\) once more. For the first two use the
positive cosh series and \(\pi<22/7\); for the last two the positive
exponential series through degree four suffices. The summed real
parts are still in \((.553,.813)\), so both real sine factors
exceed \(1/2\). Raising the height from \(c\) to \(H\ge0\)
is still favorable at fixed \(e_*\). Thus
\(A_0>199/250>3/4\), exactly as before.

Consequently the literal inequality (21) holds for either next type
after replacing \(C_{0,N}^{\rm end}\) by \(C_{\epsilon,N}^{\rm end}\)
and multiplying its left side by
\(|d_N(Y)|^{\epsilon/2}\), with the corresponding original action
and tangent on the right. This is a modulus allocation, not a
holomorphic square root of \(d_N\). When \(\epsilon=1\), the
actual negative outgoing height gives its original upper rate
\(-\Re g(b)/2\). Both parities, the whole cap, and all fixed
ordinary-color derivatives remain included. No bound for the
remaining next-four central or boundary profiles is inferred.
