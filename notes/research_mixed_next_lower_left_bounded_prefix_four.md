# Attaching a type-four block to a bounded preceding factor

Private research proof, 8 November 2026. A sufficiently small preceding
factor remains small after attachment of the complete next type-four
sum, throughout the shared interval \(0\le q\le11/50\). The preceding
factor need not itself be a complete conditional sum. This permits
the existing estimates for several discarded rows and contour terms
to be used on this larger interval.

The proof transports the next sum's controlling profiles from
\(q=11/50\). Its last-row profile need not be monotone. We bound its
total increase explicitly and deduct that increase from the already
proved margin for the preceding factor.

## 1. Statement and normalization

Use the actual ordinary references for the first three blocks of
types \((3,4,4)\), as in
[the complete lower central interval](research_mixed_next_complete_lower_plateau.md),
Section 1. Thus the shared coordinate and the next outgoing coordinate
have the form
\[
y=q+ih_y,\qquad z=u+ih_z,\qquad
0\le q\le q_0=\frac{11}{50},\qquad
u\in P=[11/50,9/20].
\tag{1}
\]
The heights are those of the same actual reference:
\[
-.102<h_y<-.001,\qquad -.108\le h_z,h_t<0.
\tag{2}
\]
Here \(h_t\) is the height used for the next conditional index.
All correlations imposed on the reference remain in force.

For an integer level \(N\ge2\), retain
\[
\begin{gathered}
r=e^{-2\pi i/N},\qquad
P_j=(r;r)_j,\qquad p_j(V)=(rV;r)_j,\\
Y=e^{-2\pi iy},\qquad Z=e^{-2\pi iz},\\
C_{1,N}(Y,Z)=\sum_{j=0}^{N-1}
                 \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^3}.
\end{gathered}
\tag{3}
\]
The Fourier polynomial \(d_N\) is the original polynomial of degree
at most \(N-1\), specified by \(d_N(r^b)=P_b^{-1}\) for \(0\le b<N\).
Let \(\Lambda_{123}(z)\) be the affine bound for the action of this
same reference, defined in the cited note, equations (6) and (9) of
its cited source. In particular its value at \(z_*\) is the real part
of the original next action, less the outgoing halfweight allocation.
No constant in this action is changed.

Set
\[
B_0=\frac{2383}{1500}.
\tag{4}
\]
Let \(V_N\) be any preceding factor, possibly depending on additional
parameters, for which, for every \(\tau>0\), a uniform bound
\[
|V_N|\le C_\tau N^{b_\tau}e^{N(B_0+\tau)}
\tag{5}
\]
holds on the domain under consideration. The additional parameters
can include the first incoming coordinate, an integration parameter
or an ordinary color. They must not alter the actual reference used
in (1)--(2) or its action bound.

**Theorem.** Under these hypotheses, there are constants \(C,b\) such
that, for all sufficiently large integer levels of both parities,
\[
\boxed{\quad
|V_Nd_N(Y)C_{1,N}(Y,Z)|\,|d_N(Z)|^{1/2}
\le C N^b
       \exp\!\left[N\left\{\Lambda_{123}(z)-\frac1{100}\right\}\right].
\quad}
\tag{6}
\]
The constants are uniform over every parameter set for which (5)
is uniform. The estimate includes the complete next sum, all of its
physical indices, and the closed endpoint \(q=0\).

Only an upper bound for \(V_N\) is required. In particular, a bound
for an absolute sum can be used for \(V_N\). A bound for a signed sum
does not thereby become a bound for its individual summands.

## 2. The available margin at \(q=q_0\)

Write \(\alpha=\Re y_*\), and let \(A_*,p,B_3(q,u)\) be the
original preceding action, its real outgoing derivative, and the
next conditional supporting function. They satisfy
\[
A_*+p(q-\alpha)+B_3(q,u)\le\Lambda_{123}(z).
\tag{7}
\]
These quantities, including their allocations, are defined in
[the low-cardinal localization theorem](research_mixed_next_low_cardinal_paired_localization.md),
Section 2.

The next bare phase is
\[
Q_1(t;y,z)=g(y+t)+g(z+t)-3g(t)-g(y)-g(z)+2\pi iyt.
\tag{8}
\]
At \(q=q_0\), each original main profile, the real cut profiles
\(t=1/8,1/2\), and the last-row profile satisfies its supporting
bound after allocation of \(-\Re g(y)/2-\Re g(z)/2\).
This is the profile-by-profile assertion in the proof of
[ordinary source assembly](research_mixed_three_row_source_assembly.md),
Section 2, rather than an inference from a bound for the signed sum.
For the last row its bare rate is
\(\delta_y=-2\pi h_y\), because both outside heights are negative.
Thus every one of these allocated profiles is at most \(B_3(q_0,u)\).

On the original plateau, \(-\Re g(y)\le-J(q)\), where
\(J(q)=\Re g(q)\). The marginal bounds of
[the low conditional block](research_mixed_conditional_lower_output_low_block.md),
equations (9)--(10), give the following reserves after replacing
the preceding factor by \(B_0\):
\[
\begin{array}{c|c}
p\le0&
\displaystyle \frac74-B_0-\frac{11}{80}
                  =\frac{143}{6000}>\frac1{50}\\[2mm]
p\ge0&
\displaystyle \frac74+\frac1{45}-B_0-\frac1{12}
                    -\frac{801}{10000}
                  =\frac{1811}{90000}>\frac1{50}.
\end{array}
\tag{9}
\]
The second line uses the same strict bound
\(A_*>7/4+819/35200>7/4+1/45\) as that source.

Consequently, at \(q_0\), the total profiles
\[
\begin{split}
\mathcal A(t;q,u)
  &=B_0+\Re Q_1(t;y,z)-\Re g(y)-\tfrac12\Re g(z),\\
\mathcal A_{\mathrm{last}}(q,u)
  &=B_0+\delta_y-\Re g(y)-\tfrac12\Re g(z)
\end{split}
\tag{10}
\]
are all strictly less than \(\Lambda_{123}(z)-1/50\).
The margin \(1/50\) comes from (9). We have not assigned a numerical
margin to the separate last-row supporting inequality.

## 3. Transport of the main and two real cut profiles

The estimates in
[the first-last comparison](research_mixed_next_lower_left_first_last_four_reduction.md),
Sections 2--4, apply unchanged to (10). Its preceding factor is
independent of \(q\); replacing that factor by \(B_0\) changes none
of those derivative calculations or index comparisons.

For clarity, the comparisons used are as follows. At its original
height \(h_t\), a main index outside \([1/6,9/20]\) can be moved
into that interval while increasing its real phase. At a fixed
index in this interval,
\[
\partial_q\mathcal A(t;q,u)
=\log|e^{-2\pi h_t}-R e^{-2\pi i(q+\Re t)}|
                 -2\log|1-R e^{-2\pi iq}|>0,
\qquad R=e^{2\pi h_y}.
\tag{11}
\]
The same strict positivity holds at the real low cut \(t=1/8\).
The referenced proof gives the explicit polynomial inequalities
on the full containing radius interval \(1/2\le R\le1\).
These profiles are therefore bounded by their values at \(q_0\).

At the real half cut, the derivative is
\[
f_R(q)=\tfrac12\log(1+R^2+2R\cos2\pi q)
                    -\log(1+R^2-2R\cos2\pi q).
\tag{12}
\]
The same proof establishes \(f_R(q)>0\) for \(q\le16/75\)
and \(f_R(q)>-1/15\) everywhere. The remaining interval has
length \(q_0-16/75=1/150\). Hence
\[
\mathcal A(1/2;q,u)
\le\mathcal A(1/2;q_0,u)+\frac1{2250}
<\Lambda_{123}(z)-\frac1{50}+\frac1{2250}.
\tag{13}
\]
This increase is charged against the explicit margin (9).

## 4. The maximum increase of the last-row profile

Only one term of \(\mathcal A_{\mathrm{last}}\) varies with \(q\).
Put
\[
\nu_R(q)=-\Re g\left(q+\frac{i\log R}{2\pi}\right).
\tag{14}
\]
The original primitive has derivative
\(g'(y)=\log(1-e^{-2\pi iy})\) on this lower branch. Therefore
\[
\nu_R'(q)=-\log|1-R e^{-2\pi iq}|.
\tag{15}
\]
For \(1/2\le R<1\) the unique maximum on \([0,q_0]\) occurs at
\[
q_R=\frac{\arccos(R/2)}{2\pi}.
\tag{16}
\]
Indeed the modulus in (15) increases with \(q\) on this interval
and equals one exactly when \(\cos(2\pi q)=R/2\).
Moreover \(1/6<q_R<q_0\). For the upper inequality,
\(\cos(2\pi q_0)=\sin(3\pi/50)<1/5<R/2\).

The maximum increase relative to \(q_0\) is consequently
\[
M(R)=\nu_R(q_R)-\nu_R(q_0)
    =\int_{q_R}^{q_0}\log|1-R e^{-2\pi is}|\,ds.
\tag{17}
\]
It is increasing in \(R\). To see this, differentiate (17).
The moving-endpoint term vanishes, since the integrand at \(q_R\)
is zero. On the remaining interval,
\[
\partial_R\log|1-R e^{-2\pi is}|
  =\frac{R-\cos(2\pi s)}{1+R^2-2R\cos(2\pi s)}>0,
\tag{18}
\]
because \(\cos(2\pi s)\le R/2\). The integral is continuous up
to \(R=1\); its limiting interval \([1/6,q_0]\) stays away
from every logarithmic zero.

Finally, the strictly concave function
\(\log(2\sin\pi s)\) has value zero and derivative \(\pi\sqrt3\)
at \(s=1/6\). Its tangent there gives
\[
\begin{split}
M(R)&\le M(1)
 =\int_{1/6}^{q_0}\log(2\sin\pi s)\,ds\\
&<\frac{\pi\sqrt3}{2}(q_0-1/6)^2
 =\frac{8\pi\sqrt3}{5625}
 <\frac{44}{5625}<\frac1{125}.
\end{split}
\tag{19}
\]
Here \(q_0-1/6=4/75\), \(\pi<22/7\), and \(\sqrt3<7/4\).
It follows that
\[
\mathcal A_{\mathrm{last}}(q,u)
<\Lambda_{123}(z)-\frac1{50}+\frac1{125}
=\Lambda_{123}(z)-\frac3{250}.
\tag{20}
\]
This is the smallest margin among the controlling profiles above.

## 5. From profiles to the complete finite sum

The [low-block theorem](research_mixed_next_lower_left_low_physical_blocks.md),
Section 2, bounds the absolute sum of all rows
\(0\le j\le\lfloor N/8\rfloor\) by the real low profile.
The [complete-current theorem](research_mixed_next_lower_left_complete_currents.md),
Sections 3, 5 and 6, bounds the middle finite sum by its main and
real cut profiles. Its exact decomposition includes the main
integral, both horizontal remainders, four weighted sides and both
unweighted joins, with their original orientations and sampling
factors. All these comparisons allow multiplication by an
index-independent preceding factor.

The [upper-row theorem](research_mixed_next_lower_left_own_four_upper_rows.md),
Section 3 and equation (13), bounds the absolute sum of all rows
\(\lceil N/2\rceil\le j<N\) by the larger of the real half and
last profiles. The intervening middle indices are exactly those
in the complete-current theorem. Thus every index in (3) is
included at both parities.

The shared weight satisfies
\[
|d_N(Y)|\le C_\tau N^{b_\tau}e^{N(-\Re g(y)+\tau)}
\tag{21}
\]
on the entire closed interval (1), by Section 3 of the low-block
theorem. This bound retains the actual Fourier polynomial,
including its forcing term at \(q=0\). The original factorial
continuation supplies the canonical middle-row formula there.
At the outgoing coordinate the usual lower-height bound gives
the allocation \(-\Re g(z)/2\).

Equations (11), (13) and (20) therefore bound the complete product
by a polynomial times \(e^{N(\Lambda_{123}-3/250+\varepsilon)}\),
where the sum \(\varepsilon\) of all prescribed rate tolerances
can be arbitrarily small. Choose it smaller than \(1/500\).
This proves (6).

Fixed powers of \(N\), and integration over a fixed chain of
uniformly bounded length in additional parameters, preserve (6)
with a possibly different polynomial prefactor. Claims about
derivatives in those parameters require the corresponding
neighborhood hypothesis for \(V_N\); they are not inferred from
an arbitrary pointwise bound (5).

## 6. Consequences and remaining work

Any previously established preceding-factor bound with rate at most
\(B_0\), valid for \(|Y|\le1\), can now be attached to the whole
next type-four sum on (1). Examples include the positive low and
upper row groups on the first incoming rectangle
\(1/2\le\Re a\le7/10\), \(-9/125\le\Im a\le0\), proved in
[the low-block theorem](research_mixed_conditional_lower_output_low_block.md)
and [the upper-block theorem](research_mixed_conditional_lower_output_upper_block.md).
Their preceding-factor rates are respectively \(2383/1500\) and
\(32563/21000<2383/1500\), with the complete cap retained.

The full contour correction polynomial of
[the lower central theorem](research_mixed_next_complete_lower_plateau.md),
equation (18), also qualifies: its disk rate is \(77/50<B_0\).
Thus its product with the next type-four factor is now controlled
on this lower-left interval as well.

The theorem does not bound a preceding contribution for which (5)
is unavailable. In particular it does not complete the first
incoming contour, does not treat a next type-three block, and does
not estimate the other complementary outgoing intervals. It gives
no lower bound for the complete signed transfer.
