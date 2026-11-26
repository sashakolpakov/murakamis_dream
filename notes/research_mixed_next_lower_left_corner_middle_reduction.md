# The incoming corner reduced to its middle integral

Private research proof, 8 November 2026. On the incoming corner
rectangle, the first conditional sum can be reduced to its real
middle integral for the entire shared interval \(0\le q\le11/50\).
The discarded physical rows and all six weighted contour terms
remain strictly smaller after the complete next type-four sum is
attached. The middle integral is retained without a critical-point
approximation.

The earlier corner reduction assumed \(q\ge11/50\). Its lower
argument estimates need modification here: the outgoing argument
can now be positive after the incoming numerator has crossed its
first integer. We compare that argument with the own-index argument
before bounding the remaining terms.

## 1. The exact integral and the desired remainder bound

Keep the actual ordinary-next references, outgoing action
\(\Lambda_{123}(z)\), and next type-four factor of
[the bounded-prefix theorem](research_mixed_next_lower_left_bounded_prefix_four.md).
The additional incoming coordinate ranges over
\[
a=x-i\eta,\qquad
\frac12\le x\le\frac7{10},\qquad 0\le\eta\le\frac9{125}.
\tag{1}
\]
The other two coordinates are
\[
y=q+ih_y,\qquad 0\le q\le11/50,\qquad -.102<h_y<-.001,
\qquad
z=u+ih_z,\quad u\in[11/50,9/20],\quad -.108\le h_z<0.
\tag{2}
\]
All reference correlations are unchanged. The variables \(x,\eta\)
are independent targets within (1), not new geometric references.

At integer level \(N\ge2\), put
\[
\begin{gathered}
r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad p_j(V)=(rV;r)_j,\\
X=e^{-2\pi ia},\qquad Y=e^{-2\pi iy},\qquad Z=e^{-2\pi iz},\\
C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
                 \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},\\
L_N=\lfloor2N/25\rfloor+1,\qquad M_N=\lceil N/2\rceil,\\
\ell_N=(L_N-1/2)/N,\qquad b_N=(M_N-1/2)/N .
\end{gathered}
\tag{3}
\]
For all sufficiently large \(N\), \(3/40<\ell_N<b_N\le1/2\).
The canonical row function is the same one used in
[the original corner reduction](research_mixed_conditional_lower_output_middle_reduction.md):
\[
T_N(s;a,y)=e^{2\pi iNas}
 \Pi_N(a+s)\Pi_N(y+s)E_N(a)E_N(y)E_N(s)^3.
\tag{4}
\]
It is exactly the summand of (3) at \(s=j/N\). Here
\(\Pi_N,E_N\) are the original factorial interpolation and its
reciprocal; their normalizations are unchanged.

**Theorem.** There is an exact decomposition
\[
C_{1,N}(X,Y)=N\int_{\ell_N}^{b_N}T_N(t;a,y)\,dt
                         +\mathcal E_N(a,y).
\tag{5}
\]
The error consists of all physical rows outside
\(L_N\le j<M_N\), together with the two horizontal and four
vertical weighted terms of the original cotangent identity at
auxiliary heights \(-2,+2\). For every \(\tau>0\),
\[
|U_{0,N}(w,X)\mathcal E_N(a,y)|
\le C_\tau N^{B_\tau}
               e^{N(2383/1500+\tau)},\qquad w\in[-2,2].
\tag{6}
\]
Consequently
\[
\boxed{\quad
|U_{0,N}(w,X)\mathcal E_N(a,y)d_N(Y)C_{1,N}(Y,Z)|
                 |d_N(Z)|^{1/2}
\le C N^B e^{N\{\Lambda_{123}(z)-1/100\}}.
\quad}
\tag{7}
\]
These statements hold uniformly on (1)--(2), including \(q=0\),
and for levels of both parities. The cap and next conditional sum
are complete.

The integral in (5) has not been estimated by (7). In particular
the theorem does not yet bound the incoming corner contribution
or give an asymptotic expansion for it.

## 2. The original upper rate across the incoming integer

Let
\[
Q(s;a,y)=g(a+s)+g(y+s)-3g(s)-g(a)-g(y)+2\pi ias,
\qquad g'(z)=\operatorname{Log}(1-e^{-2\pi iz}),
\tag{8}
\]
with the original primitive and continued strip branches. For a
numerator argument define its continuous upper rate by
\[
\mathfrak p(\zeta)=
\begin{cases}
\Re g(\zeta),&0<\Re\zeta\le1,\\
\Re g(\zeta-1)+2\pi(\Im\zeta)_+,&1\le\Re\zeta<2.
\end{cases}
\tag{9}
\]
The boundary values agree. On \(s=t+i\sigma\), set
\[
\widehat R(t,\sigma)=
\mathfrak p(a+s)+
\Re\{g(y+s)-3g(s)-g(a)-g(y)+2\pi ias\}.
\tag{10}
\]
The exact identity
\(\Pi_N(\zeta+1)=(1-e^{-2\pi iN\zeta})\Pi_N(\zeta)\)
is the source of the second term in (9). Both terms of that
identity are retained. The original zero-safe reflection estimate
at \(\Re(a+s)=1\) gives, for every prescribed rate tolerance,
\[
|T_N(t+i\sigma;a,y)|
\le C_\tau N^{B_\tau}e^{N(\widehat R(t,\sigma)+\tau)}
\tag{11}
\]
on \(\ell_N\le t\le b_N\), \(-2\le\sigma\le2\).
This is precisely the upper estimate in Section 1 of the earlier
reduction, with its outgoing real-part restriction reconsidered.

Indeed, the shifted outgoing real part now lies in
\([3/40,18/25]\), still strictly within its original strip.
Only the unshifted argument \(y\) reaches real part zero.
Its height stays strictly negative, and
[the inward-seam factorial theorem](research_factorial_symbol_across_inward_seam.md)
continues \(E_N(y)\) with the same phase and normalization.
All other denominator arguments remain in regular compact strips.
Thus (11) holds on the closed interval in (2). It asserts an
upper estimate at numerator zeros, not a nonzero local symbol there.

For real \(r\in(0,1)\), write
\[
A(r,h)=\operatorname{Arg}(1-e^{2\pi h-2\pi ir})
\tag{12}
\]
on the original strip. It lies between zero and
\(\pi(1-2r)\); for \(h\le0\) it lies between zero and
\(\pi(1/2-r)\). Bounds at a strip endpoint are taken as
the appropriate one-sided limits of (9).

## 3. Upper vertical slopes

First suppose \(x+t<1\). For \(\sigma\ge0\), differentiating
(10) and using (12) gives
\[
\begin{split}
\partial_\sigma\widehat R
&=-A(x+t,\sigma-\eta)-A(q+t,\sigma+h_y)
                      +3A(t,\sigma)-2\pi x,\\
\frac1\pi\partial_\sigma\widehat R
&\le 2-4t+\max(2q+2t-1,0)\le\frac{17}{10}.
\end{split}
\tag{13}
\]
The incoming shifted real part is at least \(1/2\).
If \(q+t\le1/2\), the last upper bound follows from
\(t\ge3/40\). Otherwise the expression is
\(1-2t+2q\le129/100<17/10\).

Now suppose \(x+t\ge1\), and put \(r_0=x+t-1\in[0,1/5]\).
The exact derivative, including the continued numerator, is
\[
\partial_\sigma\widehat R
=-A(r_0,\sigma-\eta)-A(q+t,\sigma+h_y)
       +3A(t,\sigma)-2\pi x
       +2\pi{\bf1}_{\{\sigma>\eta\}}.
\tag{14}
\]
Here \(t\ge1-x\ge3/10\).
For \(0\le\sigma\le\eta\), the incoming argument is nonnegative,
so
\[
\frac1\pi\partial_\sigma\widehat R
\le3-6t-2x+\max(2q+2t-1,0).
\tag{15}
\]
If \(q+t\le1/2\), this is at most \(-3+4x\le-1/5\).
Otherwise it is at most \(-2+2x+2q\le-4/25\).

For \(\sigma\ge\eta\), use
\(A(r_0,\sigma-\eta)\ge\pi(1/2-r_0)\) and retain
the \(2\pi\) term in (14). This gives
\[
\frac1\pi\partial_\sigma\widehat R
\le\frac72-x-5t+\max(2q+2t-1,0).
\tag{16}
\]
The two alternatives are at most
\(-3/2+4x\le13/10\) and
\(-1/2+2x+2q\le67/50\), respectively.
Combining (13)--(16) proves the uniform bound
\[
\partial_\sigma\widehat R\le17\pi/10
\qquad(\sigma\ge0).
\tag{17}
\]
These inequalities hold on each side of a possible kink in (9)
and can be integrated through it.

## 4. Lower vertical slopes

Suppose first \(x+t<1\) and \(\sigma\le0\).
The incoming argument is nonpositive, and the own argument is
nonnegative. The outgoing argument is at most
\(\pi(1/2-q-t)_+\), because its height is negative.
Consequently
\[
\frac1\pi\partial_\sigma\widehat R
\ge-2x-(1/2-q-t)_+\ge-\frac{73}{40}.
\tag{18}
\]
The last bound uses \(x\le7/10\), \(t\ge3/40\), and \(q\ge0\).

After the incoming integer, \(t\ge3/10\). The useful comparison is
\[
A(q+t,\sigma+h_y)\le A(t,\sigma)
\qquad(\sigma\le0).
\tag{19}
\]
If \(q+t\ge1/2\), the left side is nonpositive and the right
side is nonnegative. Otherwise both real parts lie in
\([3/10,1/2]\). At a fixed radius \(0<U\le1\), the argument
decreases with its real coordinate there: its derivative has the
sign of \(U\cos(2\pi t)-U^2<0\). Reducing the radius from
\(U=e^{2\pi\sigma}\) to \(Ue^{2\pi h_y}\) also reduces
this positive argument. This proves (19).

There is no continuation term in (14) for \(\sigma\le0\).
Using (19) before discarding the remaining own arguments yields
\[
\begin{split}
\frac1\pi\partial_\sigma\widehat R
&\ge-(1/2-r_0)-2x\\
&=-3/2-x+t
\ge-1/2-2x\ge-19/10.
\end{split}
\tag{20}
\]
This is valid even when the outgoing argument is positive.
For \(\sigma\le-1/8\), the incoming radius is less than \(1/2\),
so its argument is at most \(\pi/6\). The same comparison (19)
then improves (20) to
\[
\partial_\sigma\widehat R\ge-47\pi/30
\qquad(x+t\ge1,\ \sigma\le-1/8).
\tag{21}
\]
The elementary radius witness is \(e^{-\pi/4}<1/2\), as in the
earlier corner reduction.

Equations (17)--(21) imply that every weighted vertical rate
\(\widehat R(t,\sigma)-2\pi|\sigma|\) decreases away from
its real endpoint. Its loss is at least \(3\pi\sigma/10\)
above zero. Below zero the loss per unit downward distance
is at least \(7\pi/40\) before the incoming integer and
\(\pi/10\) after it, improving to \(13\pi/30\) after
downward distance \(1/8\).

## 5. Absolute estimates for all discarded finite terms

The earlier physical estimates were uniform over \(|Y|\le1\).
Thus they apply on the whole of (2). With the complete cap
attached, the positive low and upper sums have respective rates
\[
\frac{2383}{1500},
\qquad
\frac{32563}{21000}<\frac{2383}{1500}.
\tag{22}
\]
The sources are
[low conditional rows](research_mixed_conditional_lower_output_low_block.md),
equation (7), and
[upper conditional rows](research_mixed_conditional_lower_output_upper_block.md),
equation (14). Both retain all real ordinary colors and every
indicated physical row.

The real canonical endpoint rates obey these same estimates.
The limiting lower cut is \(2/25\), where its rate is at most
\(139/250\) before the cap. The limiting upper cut is \(1/2\),
where the upper-row proof applies. Uniform continuity of the
integrated rate (10), including its numerator zeros, absorbs the
\(O(1/N)\) half-grid changes with any prescribed tolerance.
The vertical inequalities therefore bound all four weighted
half-sides by these real endpoint rates. On their half-grid
lines the exact cotangent factors are bounded by
\(2e^{-2\pi N|\sigma|}\).

For the horizontal terms, the elementary real-row bound is
\[
\widehat R(t,0)<\frac{17}{10}t-3J(t)<\frac{27}{20},
\qquad \ell_N\le t\le b_N,
\tag{23}
\]
where \(J(t)=\Re g(t)\).
It uses the folded incoming modulus \(<13/5<e\), the outgoing
modulus at most two, and the original bound \(-J(t)<1/6\).
It has no restriction on the outgoing angle.

At upper height \(2\), (17) leaves a loss of at least \(3\pi/5\).
At lower height \(-2\), the loss before the incoming integer is
at least \(7\pi/20\). After it, (20)--(21) give
\[
\frac{\pi}{10}\frac18+\frac{13\pi}{30}\frac{15}{8}
=\frac{33\pi}{40}>\frac{7\pi}{20}.
\tag{24}
\]
The complete cap has rate \(1549/1500\) on (1).
Each horizontal error therefore has a preceding-factor rate less than
\[
\frac{1549}{1500}+\frac{27}{20}-\frac{7\pi}{20}
<\frac{15467}{12000}<\frac{13}{10}<\frac{2383}{1500}.
\tag{25}
\]
The first comparison uses \(\pi>25/8\).
The horizontal cotangent factors have the same exponential loss
as the vertical ones, with a fixed constant multiplier.

Apply the original split cotangent identity to the exact middle
index range in (3):
\[
\begin{split}
\sum_{j=L_N}^{M_N-1}T_N(j/N)
={}&N\int_{\ell_N}^{b_N}T_N(t)\,dt\\
&+\frac{N}{2i}\left\{
 \int_{\partial R^+}T_N(s)[\cot(\pi Ns)+i]\,ds
 +\int_{\partial R^-}T_N(s)[\cot(\pi Ns)-i]\,ds
\right\}.
\end{split}
\tag{26}
\]
The upper and lower rectangles have heights \(2,-2\).
Each displayed half-boundary omits its real edge and retains
its induced orientation. Their union gives exactly the two
horizontal and four vertical weighted terms just bounded.
The canonical numerator remains holomorphic across its integer;
its zeros create no additional residue.

Adding the actual low and upper physical sums to the remainder
in (26) defines \(\mathcal E_N\) and proves (5).
Equations (22)--(25), with finite sums and factors of \(N\)
absorbed into a polynomial, prove (6).

## 6. Attachment and remaining integral

Use \(V_N=U_{0,N}(w,X)\mathcal E_N(a,y)\) in the bounded-prefix
theorem. Equation (6) verifies its full hypothesis, uniformly in
the extra incoming parameters \(x,\eta,w\). It gives (7) with
the complete next sum and the original shared Fourier polynomial.
That theorem supplies the distinct forced bound for \(d_N(Y)\)
through \(q=0\); it does not replace it by \(E_N(y)\).

Fixed additional factors of \(N\), or integration over a bounded
incoming chain in (1), preserve the estimate with a different
polynomial prefactor. No assertion about parameter derivatives
is needed here.

The remaining corner problem is now explicitly
\[
N\,U_{0,N}(w,X)\int_{\ell_N}^{b_N}T_N(t;a,y)\,dt,
\tag{27}
\]
with the complete next factor and weights attached. A deformation
of this integral must keep both unweighted joins and compare the
actual critical action with the same \(\Lambda_{123}\). Neither
that deformation nor its action comparison is supplied by the
weighted estimates above.
