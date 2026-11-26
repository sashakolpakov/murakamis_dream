# The continued upper-cap alias at the real right endpoint

Private written deduction, 10 November 2026. The original upper
cap sampling correction has endpoint rate less than \(9/10\).
For each fixed private point on that correction, its rate on
the real incoming half-period is bounded by the larger of its
original half-face rate and this endpoint ceiling. The exact
numerator period factor is retained.

This is a bound for the specified upper-alias profile. It does
not replace the other cap currents, calibrate a conditional
kernel, or assert a completed outer period.

## 1. Original coefficient and continued alias

Retain the complete endpoint coefficient and its original
canonical phase from
[the endpoint rectangle theorem](research_mixed_endpoint_cap_rectangle.md):
\[
 \begin{split}
 F(e,v)&=-2J(1/2-v)-3J(v)-J(e-v)+i\pi ev,\\
 S(e)&=F(e,v_c(e)),\qquad F_v(e,v_c(e))=0,\\
 v_c(e)&=\frac1\pi\arctan
                 \frac{i+\sqrt{1-2e^{2\pi ie}}}{2}.
 \end{split}
 \tag{1}
\]
The square root, arctangent and logarithmic lift are those of
that source. On
\[
 \mathcal E_+=[27/100,49/100]+i[0,1/25]
 \tag{2}
\]
it supplies
\[
 \frac{17}{100}<\Re v_c<\frac7{25},\quad
 \Im v_c>0,\quad 0<\Re(e-v_c)<\frac12 .
 \tag{3}
\]
Use \(J'=\Log(2\sin\pi\cdot)\), on the original strip branch,
and \(g(z)=J(z)+i\pi(z-z^2)/2\).

The exact retained type-four cap interpolant in
[the lower-right cap proof](research_mixed_first_four_cap_lower_right_horizontal.md)
is
\[
 \mathscr A_{1,N}(e,a,w)=
 D_N(e)^{-1}\mathcal C_N(e,w)
             \frac{\Pi_N(a+e)}{\Pi_N(a)\Pi_N(e)}.
 \tag{4}
\]
No interpolation from physical values is being substituted in
(4). Its coefficient, carrier and all factorials are the
original functions. The numerator satisfies the exact recurrence
\[
        \Pi_N(q+1)=(1-e^{-2\pi iNq})\Pi_N(q).
 \tag{5}
\]
This is the product of the original \(N\) single-step
factorial recurrences. It is an identity of their continued
functions, not just an identity at integral indices.

Let \(e=u+i\eta_+\), with \(\eta_+=1/25\), and let
the incoming variable \(a=x\) be real. For \(1/2\le x<1\)
the numerator \(x+e\) crosses at most one period wall.
Define its continuous upper rate by
\[
 \mathfrak p(q)=
 \begin{cases}
 \Re g(q),&0<\Re q\le1,\\
 \Re g(q-1)+2\pi\Im q,&1\le\Re q<3/2,
 \end{cases}
 \qquad \Im q=\eta_+.
 \tag{6}
\]
In the second line the full multiplier in (5) has rate
\(2\pi\eta_+\); its modulus is bounded above and below by
fixed positive multiples of \(e^{2\pi N\eta_+}\).
The shifted real part stays in the original factorial strip.
At the wall use the continuous nonreal limits of the original
factorial rate. Thus (6) is precisely the one-period
continuation already used in the cited cap proof, with the
same recurrence now carried through the rest of this half-period.

After its actual sampling penalty is included, the upper
horizontal alias has rate
\[
 A_+(e,x)=
 \Re\{S(e)+J(e)-2g(e)\}
          +\mathfrak p(x+e)-J(x)-2\pi\eta_+.
 \tag{7}
\]
All coefficients and penalties in (7) are those of (4).
The limit at \(x=1\) exists as a rate and is exactly
\[
 A_+(e,1)=\Re\{S(e)+J(e)-g(e)\}
        =\Re\{S(e)-i\pi(e-e^2)/2\}.
 \tag{8}
\]
In particular the \(2\pi\eta_+\) numerator term in (6)
cancels the sampling penalty. It is not discarded.
The endpoint value in (8) is a continuous-rate limit;
finite estimates involving \(\Pi_N(a)^{-1}\) remain on
fixed compact intervals \(x\le1-\rho<1\).

## 2. The canonical critical height stays above the cap index

**Lemma 1.** On (2),
\[
                         \Im v_c(e)>\Im e.
 \tag{9}
\]

*Proof.* At \(\Im e=0\), (3) gives strict inequality.
Fix \(\Re e=u\) and suppose a first crossing occurs at
\(e=u+i\eta\), \(v_c=q+i\eta\), with \(0<\eta\le1/25\).
The real part of \(e-v_c\) lies in \((0,1/2)\), so
\(J'(e-v_c)\) is real. Taking the imaginary part of
the original zero-lift equation in (1) gives
\[
 \pi u=
 3\arctan\!\bigl(\cot(\pi q)\tanh(\pi\eta)\bigr)
 +2\arctan\!\bigl(\tan(\pi q)\tanh(\pi\eta)\bigr).
 \tag{10}
\]
Indeed \(J'(1/2-v_c)=\Log(2\cos\pi v_c)\);
this cosine has negative argument, while the sine in
\(J'(v_c)\) has positive argument. Both sines and cosines
have positive real parts here, so these arguments are the
displayed principal arctangents. There is no additional
multiple of \(2\pi\).

Put \(t=\tan(\pi q)\). The bounds (3) imply
\[
                            4/7<t<2.
 \tag{11}
\]
For the lower bound use \(\pi>25/8\) and
\(\tan y>y+y^3/3\) for \(0<y<\pi/2\):
\[
 \tan(\pi q)>
 \frac{17}{32}+\frac{(17/32)^3}{3}
 =\frac{57137}{98304}>\frac47.
 \tag{12}
\]
The cubic tangent bound follows by integrating
\(\tan' y=1+\tan^2y>1+y^2\).
For the upper bound use \(q<7/25<1/3\), whence
\(t<\sqrt3<2\).
The strictly convex function \(3/t+2t\) has maximum on
\([4/7,2]\) equal to its larger endpoint value,
\[
             \max\{179/28,11/2\}=179/28.
 \tag{13}
\]
Since \(\arctan y<y\) and \(\tanh y<y\) for \(y>0\),
the right side of (10) is strictly smaller than
\[
 \frac{179}{28}\pi\eta
 \le\frac{179\pi}{700}
 <\frac{27\pi}{100}\le\pi u.
 \tag{14}
\]
This contradiction excludes every first crossing.
Continuity of the original canonical branch on (2)
proves (9). \(\square\)

## 3. A strict upper bound for the endpoint rate

Define \(\mathcal Q(e)=S(e)-i\pi(e-e^2)/2\).
The critical equation in (1) gives the exact envelope derivative
\[
 S'(e)=-J'(e-v_c(e))+i\pi v_c(e).
 \tag{15}
\]
By (3) and Lemma 1, \(e-v_c\) has real part in
\((0,1/2)\) and negative imaginary part. Its sine lies
in the lower right quadrant. Consequently
\[
                  \Im S'(e)>\pi\Re v_c(e)>\frac{17\pi}{100}.
 \tag{16}
\]
Keeping \(u=\Re e\) fixed therefore yields
\[
 \partial_\eta\Re\mathcal Q(u+i\eta)
   =\pi(1/2-u)-\Im S'(u+i\eta)<\frac{3\pi}{50}.
 \tag{17}
\]
The real coefficient bound in equation (9) of
[the far-right envelope proof](research_mixed_initial44_far_right_physical_envelope.md)
is \(\lambda(u)=\Re S(u)<353/400\) on this interval.
Since \(\Re\mathcal Q(u)=\lambda(u)\), integration of
(17) gives
\[
 A_+(u+i/25,1)
 <\frac{353}{400}+\frac{3\pi}{1250}<\frac9{10}.
 \tag{18}
\]
For the last inequality, \(\pi<22/7\) suffices:
\(3\pi/1250<33/4375<7/400\).
No new action value has been evaluated.

For an actual initial44 reference the original allocated
negative-height half-face plane satisfies
\[
 B_*>\frac{183}{200}
 \tag{19}
\]
by [the sharper half-face floor](research_mixed_initial44_sharper_half_face_floor.md).
Thus the endpoint rate in (18) lies below that plane by more
than \(3/200\). This is a comparison with the stated plane;
it does not identify that plane with the real half-face cap
modulus or with each real half-face profile.

## 4. The fixed upper-alias profile has one minimum in the real input

**Proposition 2.** For every \(e=u+i/25\) with
\(27/100\le u\le49/100\), and every \(1/2\le x<1\),
\[
       A_+(e,x)\le\max\{A_+(e,1/2),A_+(e,1)\}.
 \tag{20}
\]
In particular,
\[
                   A_+(e,x)\le\max\{A_+(e,1/2),9/10\}.
 \tag{21}
\]

*Proof.* The original rate derivative on either side of the
numerator wall is
\[
 \partial_xA_+(e,x)=
       \log\frac{|1-qe^{-2\pi i(x+u)}|}
                       {|1-e^{-2\pi ix}|},
                \qquad q=e^{2\pi/25}.
 \tag{22}
\]
The period term and sampling penalty are independent of \(x\).
Their continuous integrated extension gives the same derivative
through the wall. We have \(1<q<4/3\), since
\[
   2\pi/25<44/175<2/7<\log(4/3).
 \tag{23}
\]
The last bound follows from the positive \(\operatorname{atanh}\)
formula.
Put \(\theta=2\pi(1-x)\in(0,\pi]\) and
\(\phi=2\pi u\in[27\pi/50,49\pi/50]\).
The squared numerator minus squared denominator in (22) is
\[
 L(\theta)=q^2-1+A\cos\theta-B\sin\theta,\qquad
 A=2(1-q\cos\phi)>0,\quad B=2q\sin\phi>0.
 \tag{24}
\]
It satisfies
\[
 L(0)>0,\qquad
 L(\pi)=q^2-3+2q\cos\phi<16/9-3<0.
 \tag{25}
\]
Moreover \(L'=-A\sin\theta-B\cos\theta\) is negative
on \([0,\pi/2]\) and has exactly one zero on
\((\pi/2,\pi)\), changing from negative to positive.
Thus \(L\) first decreases and then increases; because
its value at \(\pi\) remains negative, it has exactly
one zero on \((0,\pi)\).

Reversing the direction from \(\theta\) to \(x\), the
derivative in (22) is negative before that zero and
positive afterwards. Hence \(A_+(e,x)\) has one minimum
and its maximum on the closed rate interval \([1/2,1]\)
occurs at an endpoint. The limit at \(1\) is (8).
This proves the first inequality of (20), and (18) gives
(21) with the stated strict endpoint surplus. \(\square\)

The retained half-face entry in (21) is the actual
upper-alias profile, with its original sampling penalty.
It must be combined with its own established conditional
calibration. The second entry may instead be combined with
a separately justified comparison using the plane in (19).
The proposition does not substitute \(B_*\) for the first
entry without such an argument.

On any fixed compact incoming interval \(x\le1-\rho\),
the complete endpoint coefficient theorem, the exact
single-period identity (5), and the original factorial
upper estimates bound this literal horizontal correction
by its displayed rate, with arbitrary fixed rate allowance
and polynomial cost. Its original residue prefactor and
sampling kernel are unchanged. The same all-real-color
coefficient upper bound used in the lower-right cap proof
applies unchanged: its private coefficient argument still
lies on the very same segment of the endpoint rectangle.
The ordinary color may also range over a sufficiently
small fixed disk, by that source's polynomial continuation
argument, and fixed derivatives follow on smaller disks. This statement
concerns only the horizontal alias in (4), not any
unestimated cap side, physical row or conditional term.
No bound uniform in \(\rho\downarrow0\) is asserted.

## Direct source versions

| Direct source | SHA-256 |
|---|---|
| research_mixed_endpoint_cap_rectangle.md | 9211d45bdd031c908690a723ebcd4b40a34fed90f44858301a809ee5901c15e8 |
| research_mixed_first_four_cap_lower_right_horizontal.md | 4d41a967edabf0710fc7b04b723bb3e2fb7a407d44bb5a0fc1678e3f9ee5ee6e |
| research_mixed_initial44_far_right_physical_envelope.md | a676bfee21df1e78965bb6515a37e0aebd669b6fb4e4cecb2976a8c254cf778d |
| research_mixed_initial44_sharper_half_face_floor.md | eeb48098cf6a53eb7e9cee54ec1eb944f5607252e42550fbc69599f4a76c672a |

The complete written proof and all directly used source
implications were read, and all four source bindings were
checked. No mathematical numerical evaluation, saved-value
arithmetic, source replay, import, compilation, test or
frozen-note edit was used. Independent review is required
before adoption.
