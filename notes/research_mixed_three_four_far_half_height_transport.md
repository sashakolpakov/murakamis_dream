# Incoming-height transport for the nonpositive terminal profiles

Research deduction, 7 November 2026. On the far incoming half-circle,
raising a nonpositive incoming height to zero lowers each terminal
profile whose transform height is nonpositive. The proof retains the
original incoming chirp and logarithmic branch. It does not cover the
positive transform alias, move a whole incoming contour, or compare
the resulting profiles with the paired critical action. No numerical
evaluation is used.

## 1. The original phase and its derivative

Keep the exact ordinary \((3,4)\) source of
[the pair target](research_mixed_three_four_ordinary_pair_target.md),
equations (3)--(6). Its regular terminal interpolation has phase
\[
 \Phi(a;t,e)=S(e)+g(a+t)+g(e+t)-3g(t)-g(e)-g(a)
       -\frac{\pi i}{2}(e-e^2)+2\pi iat.
 \tag{1}
\]
Here \(S(e)\) is the action of the whole original endpoint
coefficient. The last term in (1) is the original transform chirp.
We use
\[
 a=x+ih,\quad \frac12\le x<1,\quad h\le0,\qquad
 t=u+i\eta,\quad 0<u\le\frac12,\quad \eta\le0.
 \tag{2}
\]
The private variable is unchanged; in the actual regular source
it lies in \(E_c=[.27,.49]+i[-.055,.04]\).

For the two incoming-dependent logarithms, use the original
lower-half-plane disk branch
\[
 g'(z)=\Log(1-e^{-2\pi iz}).
 \tag{3}
\]
It agrees with the original strip branch for \(0<\Re z<1\).
The global lower-half-plane continuation across the positive
factorial walls is the one proved in
[the upper-main arc note](research_mixed_fourier_right_cap_upper_main_arc.md),
Section 1. In particular (3) is not replaced by an upper-half-plane
lift when \(\Re(a+t)>1\). Here \(\Im(a+t)\le0\).
Boundary values at a zero are taken by continuity of the primitive,
not by division by its vanishing derivative factor.

The exact derivative is
\[
 \Phi_a=g'(a+t)-g'(a)+2\pi it.
 \tag{4}
\]
It is independent of \(e\), including its height and sampling
penalty.

## 2. A uniform sign with the incoming radius retained

**Lemma 1.** At every regular point of (2),
\[
                         \Im\Phi_a\ge\pi u>0.
 \tag{5}
\]

*Proof.* Set \(R=e^{2\pi h}\le1\), \(r_t=e^{2\pi\eta}\le1\).
First suppose \(x+u<1\). Compare the two numerator radii
\(Rr_t\le R\). Since \(\sin 2\pi(x+u)<0\),
\(\arg(1-\rho e^{-2\pi i(x+u)})\) decreases as \(\rho\)
increases from zero to one. Thus decreasing the shifted radius
from \(R\) to \(Rr_t\) only increases its argument.

For the same-radius quotient
\[
 Z=\frac{1-Re^{-2\pi i(x+u)}}{1-Re^{-2\pi ix}},
\]
multiply its numerator times its conjugate denominator by
\(e^{i\pi u}\). The resulting real and imaginary parts are
\[
 \begin{split}
 A&=(1+R^2)\cos\pi u-2R\cos(2\pi x+\pi u)>0,\\
 B&=(1-R^2)\sin\pi u\ge0.
 \end{split}
 \tag{6}
\]
Indeed
\(\pi+\pi u\le2\pi x+\pi u<2\pi-\pi u\), so the second
cosine is strictly smaller than \(\cos\pi u\). Here \(u<1/2\)
automatically when \(x+u<1\). The principal disk arguments,
or continuation from \(R=0\), therefore give
\[
 \arg(1-Re^{-2\pi i(x+u)})
       -\arg(1-Re^{-2\pi ix})\ge-\pi u.
 \tag{7}
\]
No multiple of \(2\pi\) is inserted. Combining the favorable
radius change with the \(+2\pi u\) imaginary part of the chirp
in (4) proves (5).

If \(1\le x+u<3/2\), the shifted disk argument is nonnegative,
whereas the incoming disk argument is nonpositive. Thus (4)
has imaginary part at least \(2\pi u\). The endpoints follow
by limits wherever (4) is defined. If a logarithmic factor
vanishes at height zero, use the continuous primitive when
integrating the conclusion. This also covers \(u=1/2\).
\(\square\)

**Corollary 2.** For \(h_0\le h_1\le0\), all other variables
fixed as in (2), the primitive satisfies
\[
 \Re\Phi(x+ih_1;t,e)
 \le \Re\Phi(x+ih_0;t,e)-\pi u(h_1-h_0).
 \tag{8}
\]
The same inequality holds after any fixed transform or private
sampling penalty is subtracted. It follows from
\(\partial_h\Re\Phi=-\Im\Phi_a\). At a height-zero numerator
wall it follows by integration below zero and continuity.

Thus (8) transports the main, lower-alias, and real-transform-cut
profiles whenever their transform heights are nonpositive. It is
uniform over the unchanged private main, cuts, aliases and sides.
It neither removes any current nor supplies a free extension of
their finite-source domains.

## 3. The remaining comparison is explicit

At incoming real part \(x=1/2\), the completed
[moving-cut theorem](research_mixed_three_four_moving_transform_cut.md)
uses transform real parts \(u\in[1/10,1/2]\).
Suppose its actual incoming height is \(c\le0\), and write \(B_U\)
for its full first-cap supporting plane. For each of its
nonpositive-transform profiles with calibrated deficit \(\delta\),
(8) gives
\[
 \frac{41}{40}+\Re\Phi(1/2;t,e)-\operatorname{pen}
 \le M-\delta+\frac{41}{40}-B_U(1/2)+\pi u c.
 \tag{9}
\]
Here \(41/40\) is the whole *physical* first-cap ceiling from
[the physical far-half theorem](research_mixed_three_four_physical_far_half.md).
It is not a bound for that cap at complex incoming height.
In particular the additional scalar inequality
\[
                   B_U(1/2)-\frac{\pi c}{10}
                                      \ge\frac{41}{40}
 \tag{10}
\]
would preserve the deficit in (9) simultaneously for all these
profiles. Equation (10) is stated as a sufficient condition,
not as a proved comparison. The original right-strip result
alone does not imply it.

The positive transform alias has \(\eta>0\), and is outside
Lemma 1. Actual references with \(c>0\) also require a separate
argument. For incoming real part \(x>1/2\), even the initial
profile comparisons at height \(c\) remain to be supplied.
Finally a bound for the remaining partial incoming root sum
requires all of its own aliases, endpoints and joins. The
height inequality (8) establishes none of those missing claims.
