# Uniform decay of the diagonal residue phase along a shear

Research deduction, 7 November 2026. The diagonal residue keeps
the sum of the retained and outgoing indices fixed. Moving their
imaginary parts in opposite directions makes its paid phase
strictly decrease, at every height. This statement uses the
original triangular index support and the original logarithmic
lifts. Its proof consists of elementary argument inequalities;
no numerical evaluation or new certificate is used.

This controls a phase along the residue fibers. Finite estimates
on their infinite ends and the complete current assembly remain
separate requirements. In particular it does not assign a bound
to a connector whose initial value has not been controlled.

## 1. The source phase on a supported total-index layer

Use the original source and phase of
[the diagonal-residue deduction](research_mixed_fourier_right_cap_diagonal_residue_source.md).
Keep the actual incoming parameter \(a=x+i h_a\), with
\[
 11/50\le x\le9/20,\qquad |h_a|\le.108,
 \qquad e^{-2\pi h_a}<2.
 \tag{1}
\]
The last bound follows from \(.216\pi<\log2\).
Write the fixed original output as
\[
 y=\xi+i\upsilon,\qquad Y=e^{2\pi iy}=\rho e^{i\phi},
 \qquad 0<\rho<5/8,\quad 0<\phi<7/6.
 \tag{2}
\]
In the actual source \(\phi=2\pi\xi\).
Let
\[
 1/8\le u\le1/2,\qquad 9/20\le z,\qquad u+z<1,
 \qquad s=u+iH,\quad q=z-iH,\quad H\ge0.
 \tag{3}
\]
Thus the total real index \(s+q=u+z\) is fixed. The physical
layers have \(u+z=\ell/N\), \(1\le\ell<N\). The bound below
is uniform as that total index tends to one.

The allocated original phase is
\[
 \mathscr F_\eta(s,a,q)=g(s+a)+g(s+q)-3g(s)
       -(1+\eta/2)g(a)-g(q)+2\pi ias+\ell_q(y),
 \tag{4}
\]
where
\[
 \ell_q(y)=2\pi iy(q-1/2)
       -\frac{\operatorname{Li}_2(Ye^{-2\pi iq})-
                    \operatorname{Li}_2(Y)}{2\pi i}.
\]
The residue current has the exact additional factor
\(e^{-2\pi iNq}\). Its paid real phase is therefore
\[
 \mathcal P_\eta(H;u,z,a)
       =\Re\mathscr F_\eta(u+iH,a,z-iH)-2\pi H.
 \tag{5}
\]

**Theorem 1.** On (1)--(3),
\[
       \frac{d}{dH}\mathcal P_\eta(H;u,z,a)<-1/20.
 \tag{6}
\]
Consequently, for every \(H_1\ge H_0\ge0\),
\[
 \mathcal P_\eta(H_1;u,z,a)
 \le\mathcal P_\eta(H_0;u,z,a)-(H_1-H_0)/20.
 \tag{7}
\]
The statement is independent of the incoming type \(\eta\),
whose allocation is constant along this shear.

## 2. Exact argument factorization

For \(R>0\) and \(0<t<1\), define
\[
                   A_R(t)=\arg(1-Re^{-2\pi it})
 \tag{8}
\]
on its original continuous principal determination. The factor
never meets the negative real axis on this open real strip:
at \(t=1/2\) it is positive, and elsewhere its imaginary part
is nonzero. For \(R\le1\), it also lies in the closed right
half-plane and
\(A_R(1-t)=-A_R(t)\).

Put \(r=e^{-2\pi H}\), so \(0<r\le1\). Direct factorization
on the same original strip gives
\[
 \begin{split}
 \Im g'(u+iH)&=\pi(1-2u)-A_r(u),\\
 \Im g'(s+a)&=\pi(1-2u-2x)
                  -A_{r e^{-2\pi h_a}}(u+x).
 \end{split}
 \tag{9}
\]
The second equality holds even when \(H+h_a\) is negative;
its radius in (8) is allowed to exceed one. It does not reset
a logarithm at a period.

Since \(\ell_q'(y)=2\pi iy-\Log(1-Ye^{-2\pi iq})\),
the shared \(g'(s+q)\) terms cancel before any estimate.
Equations (8)--(9) give exactly
\[
 \begin{split}
 P&:=2\pi+\Im(\mathscr F_{\eta,s}-\mathscr F_{\eta,q})\\
  &=4\pi u-\phi+3A_r(u)
       -A_{r e^{-2\pi h_a}}(u+x)
       +A_r(z)+A_{\rho r}(z-\xi).
 \end{split}
 \tag{10}
\]
In the actual output range, \(0<z-\xi<1\), so the last
argument has the same determination as the cardinal logarithm.
The derivative in (6) is \(-P\). The proof will show \(P>1/20\).
In particular it never differentiates the singular total-index
factor at the limit \(u+z=1\); that factor is constant in \(H\).

Two elementary disk bounds used below are
\[
 |A_r(t)|\le\arcsin r\quad(0\le r\le1),\qquad
 |A_{\rho r}(t)|<\frac7{10}r .
 \tag{11}
\]
For the second, convexity of \(\arcsin\) gives
\(\arcsin(\rho r)\le r\arcsin\rho\), while
\(\sin(7/10)>7/10-(7/10)^3/6>5/8\).
We also use \(|A_{\rho r}(t)|<\pi/4\), since
\(\rho r<5/8<1/\sqrt2\).

## 3. The retained interval \(1/4\le u\le1/2\)

On \([u,1/2]\), the derivative of \(A_r(t)\) has the sign
of \(\cos(2\pi t)-r\), and is nonpositive. If \(z\ge1/2\),
the support condition gives \(1-z\ge u\), so
\(A_r(z)=-A_r(1-z)\ge-A_r(u)\). If \(z\le1/2\), its
argument is nonnegative and the same lower bound holds.
Therefore
\[
                       3A_r(u)+A_r(z)\ge2A_r(u)\ge0.
 \tag{12}
\]

When \(u+x\ge1/2\), the subtracted argument in (10) is
nonpositive. Otherwise \(u+x\ge.47\), and its upper bound
at any positive radius is \(\pi(1-2u-2x)\le3\pi/50\).
Thus (10)--(12) imply
\[
 P>\pi-\phi-3\pi/50-\pi/4
       =69\pi/100-\phi>271/300>1/20.
 \tag{13}
\]
Only \(\pi>3\) and \(\phi<7/6\) were used in the last step.

## 4. Two auxiliary argument inequalities for \(1/8\le u\le1/4\)

On this interval the angular derivative of \(A_r(u)\)
has at most one zero, a maximum. Hence
\[
 A_r(u)\ge m(r):=
 \min\left\{\arctan r,\ \arctan\frac{r}{\sqrt2-r}\right\}.
 \tag{14}
\]
The second branch is the smaller one precisely when
\(r\le\sqrt2-1\).

**Lemma 2.**
\[
 \begin{split}
 m(r)&\ge 7r/10+3r^2/10 &&(0\le r\le1/2),\\
 \arcsin r&\le(3/2)m(r) &&(0\le r\le1/\sqrt2).
 \end{split}
 \tag{15}
\]

*Proof.* Put \(b(r)=\arctan(r/(\sqrt2-r))\). On \([0,1/2]\),
\[
 b'(r)=\frac{\sqrt2}{2-2\sqrt2r+2r^2}
                      >7/10+3r/5.
 \tag{16}
\]
For a direct rational verification, cross multiply the positive
denominator and use \(\sqrt2>7/5\). The resulting lower
difference is
\(19r/25+7r^2/25-6r^3/5\ge0\); at zero the discarded
\(\sqrt2-7/5\) is strictly positive. Integration gives the
first bound for \(b\). For the other branch,
\(\arctan r\ge r-r^3/3\ge7r/10+3r^2/10\) on this same
interval, proving the first line.

The derivative of
\((3/2)\arctan r-\arcsin r\) has the sign of
\(5-17r^2-4r^4\). It changes sign only from positive to
negative. The function therefore has its minimum at an endpoint
of \([0,1/\sqrt2]\). Its value at zero is zero, and at the
other endpoint it is positive because
\(\arctan(1/\sqrt2)>\pi/6\).
For the smaller branch \(b\), it suffices to consider
\(r\le\sqrt2-1<1/2\). On \([0,1/2]\),
\((1-r^2)^{-1/2}\le1+r\), as follows by squaring.
Equation (16) consequently gives
\[
 \frac d{dr}\{(3/2)b(r)-\arcsin r\}
             >1/20-r/10\ge0.
\]
Its value at zero is zero. This proves the second line.
\(\square\)

The subtracted first-incident argument in (10) also has a
uniform bound on the smaller retained interval:
\[
 A_{r e^{-2\pi h_a}}(u+x)
       \le\arctan t_r,\qquad t_r=\frac{5r}{3(1+r)}.
 \tag{17}
\]
If \(u+x\ge1/2\), its sign already proves this. Otherwise
\(u+x\ge.345\), and the argument increases with its radius
but decreases with its real coordinate on this range.
Its radius is at most \(2r\). Moreover
\(\cos(.69\pi)<-1/2\) and \(\sin(.69\pi)<5/6\).
Thus the tangent of its positive argument is at most
\((5r/3)/(1+r)\), proving (17).
For the sine witness, \(.19\pi>59/100\) and
\[
 1-(59/100)^2/2+(59/100)^4/24-5/6
                      =-5602639/2400000000<0.
\]
The cosine witness follows from \(.19\pi>\pi/6\).

## 5. Three radius ranges finish the uniform bound

Throughout this section \(1/8\le u\le1/4\), so
\(4\pi u-\phi>1/3\).

First suppose \(0\le r\le1/2\). Equations (11), (14)--(17)
give
\[
 P>1/3+7r/20+9r^2/20-t_r>1/20.
 \tag{18}
\]
The last inequality is equivalent, after multiplication by
\(60(1+r)\), to
\(17-62r+48r^2+27r^3>0\).
Writing \(v=2r\in[0,1]\), its exact positive representation is
\[
 17(1-v)^3+20v(1-v)^2+v^2(1-v)+(11/8)v^3>0.
 \tag{19}
\]

Next suppose \(1/2\le r\le1/\sqrt2\). Now \(m(r)=\arctan r\).
One has \(t_r<7/10\), and the alternating arctangent estimate
gives \(\arctan t_r\le t_r-t_r^3/5\).
Indeed \(t-t^3/3+t^5/5\le t-t^3/5\) for \(0\le t\le7/10\).
It follows that
\[
 P>1/3+4r/5-r^3/2-t_r+t_r^3/5>1/20.
 \tag{20}
\]
Multiplying the last difference by \(540(1+r)^3\) gives
exactly
\[
 153-9r-45r^2+r^3(779-378r-810r^2-270r^3).
 \tag{21}
\]
On this interval \(r<5/7\), \(r^2\le1/2\), and
\(r^3<5/14\). The parenthesis is greater than
\(779-270-405-675/7=53/7>0\), while
\(153-9r-45r^2>153-45/7-45/2>0\).
This proves (20) by exact rational comparisons.

Finally suppose \(1/\sqrt2\le r\le1\). On
\([u,1/2]\), \(\cos(2\pi t)\le1/\sqrt2\le r\), so the
support argument of (12) applies again. Thus
\(3A_r(u)+A_r(z)\ge2A_r(u)\ge2\arctan r\).
Equation (17) is less than \(3/4\): its tangent is at most
\(5/6\), whereas \(\tan(3/4)\ge3/4+(3/4)^3/3>5/6\).
Using (11), \(r>7/10\), and the elementary lower bound for
arctangent, we obtain
\[
 P>1/3+2\{7/10-(7/10)^3/3\}-3/4-7/10
                         =41/750>1/20.
 \tag{22}
\]
Equations (13), (18), (20), and (22) prove Theorem 1.

## 6. What remains in the residue current

The exact residue is an original total-index row multiplied by
its first outgoing Fourier harmonic. The shear leaves its total
factorial \(P_\ell\) fixed, including levels \(\ell=N-1\).
Thus (6) supplies a uniform directional phase estimate without
replacing that physical factorial by a regular-strip packet.

On any fixed finite height interval, the original finite-source
estimates transfer (7) to an exponential upper envelope with an
arbitrary fixed tolerance and a polynomial prefactor. Uniform
control of the infinite ends requires the exact factorial tail
formulas as well; it does not follow merely from a fixed-level
decay limit. The existing diagonal height comparison pays the
initial values on retained-side fibers from the corresponding
real retained cuts. The fiber at the outgoing cut \(\Re q=9/20\)
still requires its own coherent comparison with the other shifted
currents. No connector is discarded by this theorem, and no
complete right-cap or knot-volume identity is inferred.
