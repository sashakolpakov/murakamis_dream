# A calibrated three-factor affine floor for prefixes 443 and 444

Private written proof, 11 November 2026. The original affine action
for the first three factors satisfies a uniform lower bound on the
entire actual third plateau. The outgoing halfweight is kept on the
same side as the source it will calibrate:
\[
             \Lambda_{123}(z)+\frac{\beta}{2}\Re g(z)>\frac73,
                 \qquad \beta=0,1.
 \tag{1}
\]
The argument selects explicit points among the raw profiles already
bounded by the original double-selected comparison. It is not a
lower bound for a finite cap, conditional kernel, or their product.
No seam estimate or second-period completion is asserted here.

## 1. The exact profile inequality used as a lower witness

Fix an actual positive three/four word of length \(m\ge4\) beginning
with flags \((1,1,\beta)\). Keep its original coupled reference,
phases, constants and logarithmic lifts. Write
\[
 P=[11/50,9/20],\quad H=1/100,\quad
 z=v+ic_3,\quad v\in P,\qquad
 h_e=\Im e_*,\quad h_2=\Im s_2^*,\quad h_3=\Im s_3^*.
 \tag{2}
\]
The source domains give
\[
 -.051\le h_e\le-.019,\qquad -.102\le h_2\le-.001,
 \tag{3}
\]
\[
 \begin{cases}
  -.065\le h_3,c_3\le.068,&\beta=0,\\
  -.102\le h_3,c_3\le-.001,&\beta=1.
 \end{cases}
 \tag{4}
\]
The cap-height statement is part of the original double-selected
domain check. The conditional heights are the ordinary bounds in
the retained-prefix source, including when the following leg at
\(m=4\) is attached. These are bounds on the actual reference;
the references are not varied independently in this proof.

The primitives and bare phases are
\[
 J'(w)=\operatorname{Log}(2\sin\pi w),\quad J(0)=0,\qquad
 g(w)=J(w)+\frac{\pi i}{2}(w-w^2),
 \tag{5}
\]
\[
\begin{split}
 F(e,u)&=-2J(1/2-u)-3J(u)-J(e-u)+i\pi eu,\\
 S(e)&=F(e,u_c(e)),\\
 \Psi(e,a)&=S(e)+g(e+a)-g(a)-g(e)-\frac{\pi i}{2}(e-e^2),\\
 Q_\epsilon(s;a,y)&=g(s+a)+g(s+y)-(2+\epsilon)g(s)
                            -g(a)-g(y)+2\pi ias.
\end{split}
\tag{6}
\]
Every branch is the original one in the endpoint rectangle and
ordinary regular strips. Let
\[
\begin{split}
 F_{123}&=\Psi(e,z_1)+Q_1(s_2;z_1,z_2)
           +Q_\beta(s_3;z_2,z_3)
                    -g(z_1)-g(z_2)-\frac\beta2g(z_3),\\
 p_R&=g'(s_3^*+r_3)-(1+\beta/2)g'(r_3),\\
 \Lambda_{123}(z)&=\Re F_{123,*}+\Re\{p_R(z-r_3)\}.
\end{split}
\tag{7}
\]
These are exactly the action and outgoing derivative of the
[double-selected tangent theorem](research_mixed_double_selected_tangent_completion.md).

Choose the following target and profile points:
\[
        a=y=\frac14+iH,\qquad
        e=\frac38+ih_e,\qquad
        s_2=\frac14+ih_2,\qquad s_3=\frac14+ih_3 .
 \tag{8}
\]
Both outer real coordinates belong to \(P\). The cap real
coordinate \(3/8\) is in its main interval \([.27,.49]\).
The first conditional real index \(1/4\) is in \([1/8,1/2]\);
the third is in both \([3/20,1/2]\) and \([1/8,1/2]\).
Their imaginary parts are precisely the main-profile heights.
The outgoing target is every \(z\) in (2).

Thus (8) lies in the full raw main/main/main box of Theorem 1
of that tangent theorem. Choose its two factorial alternatives
\(\nu_1=\nu_2=1\), and put
\[
 A_H=-\Re g(1/4+iH),\qquad W=A_H-2\pi H,
 \tag{9}
\]
\[
 T_\beta(z)=
 \Re\Psi(e,a)+\Re Q_1(s_2;a,y)+\Re Q_\beta(s_3;y,z)+2W.
 \tag{10}
\]
The original profile inequality, before any finite summation, says
\[
 T_\beta(z)-\frac\beta2\Re g(z)
                         <\Lambda_{123}(z)-\frac1{100}.
 \tag{11}
\]
In particular, a lower bound for the explicit number (10) gives
a lower bound for the same original affine action. Equation (11)
is not recovered from a modulus estimate for a cancelling sum.
No incoming supporting plane or unrelated isolated reference is
substituted.

## 2. Quarter-line identities on the original branches

Put
\[
 b_2=-4J(1/4),\qquad
 \lambda(t)=\Re S(t),\qquad \lambda_*=\lambda(1/2).
 \tag{12}
\]
The written midpoint proof in Section 2 of the
[complete real-first-arc theorem](research_mixed_complete44_second_selected_real_first_arc.md)
gives
\[
                        b_2>\frac{23}{40},\qquad
                        \lambda_*>\frac{17}{22}>\frac{77}{100}.
 \tag{13}
\]
That proof integrates the original critical-line curvature and uses
alternating-series and positive-series inequalities. No action value
is evaluated here.

For \(k\ge0\) define
\[
                     A(k)=-\Re g(1/4-ik).
 \tag{14}
\]
The original lower-disk logarithm gives
\[
 A(0)=b_2/4,\qquad
 A'(k)=-\arctan(e^{-2\pi k}),\qquad
 A_H=A(H)+\frac{\pi H}{2}
                   \ge\frac{b_2}{4}+\frac{\pi H}{4}.
 \tag{15}
\]
The last identity is Schwarz reflection of \(J\); its inequality
uses \(A'(k)\ge-\pi/4\). The same reflection gives
\[
 \Re g(1/2+ih)=0,\qquad
 \Re g(1/4+ik)=-A(k)-\frac{\pi k}{2}.
 \tag{16}
\]
These are values of real parts on one original lift, not a change
of logarithm.

Set
\[
 V_2(k)=2A(k)+\frac{\pi k}{2},\qquad
 V_3(k)=3A(k)+\frac{\pi k}{2}.
 \tag{17}
\]
Then \(V_2'(k)=\pi/2-2\arctan(e^{-2\pi k})\ge0\), so
\[
                         V_2(k)\ge b_2/2.
 \tag{18}
\]
The derivative \(V_3'(k)=\pi/2-3\arctan(e^{-2\pi k})\) has
its unique zero at
\[
                          k_*=\frac{\log3}{4\pi},
 \tag{19}
\]
and changes from negative to positive there. Its minimum is
\[
                              V_3(k_*)=\lambda_*/2.
 \tag{20}
\]
To check the constant in (20), let
\(L(k)=\Re F(1/2,1/4+ik)\). The original midpoint identities
give \(L(0)=3b_2/2\) and
\[
 L'(k)=6\arctan(\tanh\pi k)-\pi/2.
 \tag{21}
\]
The identity
\(\arctan(e^{-2\pi k})+\arctan(\tanh\pi k)=\pi/4\)
shows \(V_3'=L'/2\); their initial constants also agree.
At (19), the point \(1/4+ik_*\) is the original endpoint
critical point, so \(L(k_*)=\lambda_*\).
This proves (20), and hence \(V_3(k)\ge\lambda_*/2\) for all \(k\ge0\).

Since \(h_2<0\), substitution in the first ordinary phase yields
the exact identity
\[
 \Re Q_1(s_2;a,y)
      =V_3(-h_2)+2A_H-\frac{\pi H}{2}
      \ge\frac{\lambda_*}{2}+2A_H-\frac{\pi H}{2}.
 \tag{22}
\]
Both shifted factorial arguments have real part one half,
so their real parts vanish by (16). The incoming chirp supplies
the displayed linear height terms.

For the third factor write
\[
                   \Delta_\beta(z)=\Re g(s_3+z)-\Re g(z).
 \tag{23}
\]
Equations (15)--(18) and (20), with the two possible signs of
\(h_3\) retained, give
\[
 \Re Q_\beta(s_3;y,z)\ge
 \begin{cases}
  b_2/2+A_H-\pi H/2+\Delta_0(z),&\beta=0,\\
  \lambda_*/2+A_H-\pi H/2+\Delta_1(z),&\beta=1.
 \end{cases}
 \tag{24}
\]
For \(\beta=0\), the part
\(-2\Re g(s_3)-\pi h_3/2\) equals \(V_2(|h_3|)\).
For \(\beta=1\), the actual height is negative and that part
with coefficient three is \(V_3(-h_3)\). Thus no
nonpositive-height condition has been imposed on an ordinary
type-three index.

## 3. The outgoing difference is positive on the full third plateau

The original disk formula and reflection, in equations (30)--(31)
of [retained-prefix calibration](research_mixed_retained_prefix_unselected_plateau.md),
show that
\[
 \Re g(t+ih)<0\quad(0<t<1/2),\qquad
 \Re g(t+ih)>0\quad(1/2<t<1)
 \tag{25}
\]
for every real \(h\), with zero at \(t=1/2\).
If \(v\ge1/4\), then \(v+1/4\ge1/2\); (25) proves
\(\Delta_\beta(z)>0\) immediately.

It remains to consider \(11/50\le v<1/4\).
For \(0<t<1/2\), \(\rho=e^{-2\pi |h|}\), the lower-disk
estimate in equation (26) of
[Fourier-weight continuation](research_mixed_fourier_weight_continuation.md)
and reflection give
\[
 -\Re g(t+ih)\ge
                 \frac{\sin(2\pi t)}{2\pi}\log(1+\rho).
 \tag{26}
\]
Here \(\sin(2\pi v)>4/5\): on this interval the sine is
increasing, and \(2\pi(11/50)>1\), while
\(\sin1\ge1-1/6=5/6\).

For \(\beta=0\), \(|c_3|\le17/250\). Thus
\(2\pi|c_3|<1/2\) and \(\rho>3/5\). One elementary
witness is
\[
 e^{1/2}<1+\frac12+\frac18\sum_{j\ge0}(1/6)^j
                   =\frac{33}{20}<\frac53.
 \tag{27}
\]
Using \(\log(8/5)>6/13\), (26) gives
\[
              -\Re g(z)>\frac{12}{65\pi}>
                            \frac{42}{715}>\frac1{20}.
 \tag{28}
\]
Put \(t=v+1/4\in[47/100,1/2)\) and \(h=h_3+c_3\).
For \(h\le0\), the radial disk formula gives
\(-\Re g(t+ih)\le-J(t)\le(1/2-t)\log2\).
For \(h>0\), reflection adds \(\pi(1-2t)h\).
Since \(h\le17/125\), both cases give
\[
 -\Re g(s_3+z)
 \le\frac3{100}\log2+\frac{51\pi}{6250}<\frac1{20}.
 \tag{29}
\]
For the last comparison use \(\log2<7/10\) and \(\pi<22/7\).
The exponential witness
\[
 e^{7/10}>
 1+\frac7{10}+\frac{49}{200}+\frac{343}{6000}
                         +\frac{2401}{240000}
  =\frac{482921}{240000}>2
 \tag{30}
\]
proves the logarithmic bound. The remaining rational comparison
is \(1122000<1268750\).
Equations (28)--(29) prove \(\Delta_0(z)>0\).

For \(\beta=1\), both \(h_3,c_3\) are negative. Also
\[
 2\pi|c_3|\le\frac{51\pi}{250}<\frac23<\log2,
 \tag{31}
\]
where \(\log2>2/3\) follows from
\(\log x>2(x-1)/(x+1)\). Thus \(\rho>1/2\), and (26) yields
\[
            -\Re g(z)>\frac{4}{25\pi}>
                              \frac{14}{275}>\frac1{20}.
 \tag{32}
\]
The sum height is negative, so
\[
              -\Re g(s_3+z)\le\frac3{100}\log2<\frac1{20}.
 \tag{33}
\]
This proves \(\Delta_1(z)>0\). All estimates used the whole
independent real third plateau at its actual height.

## 4. A lower trial for the cap with its actual private height

Let \(f(t)=\lambda(t)+J(t)\). The exact derivative identity in
Section 2 of the
[complete-column source](research_mixed_symmetric_closing_complete_column_norm.md)
is
\[
 D(t)=\sqrt{1-2e^{2\pi it}}=a(t)+ib(t),\quad a(t)>0,\qquad
 f'(t)=\frac12\log\frac{1-b(t)}{1+b(t)}.
 \tag{34}
\]
We need a curvature bound only on \(3/8\le t\le1/2\).
On this interval
\[
 a^2\ge\Re D^2=1-2\cos(2\pi t)\ge1+\sqrt2>\frac94,
 \qquad |b|=\frac{\sin(2\pi t)}a<\frac12.
 \tag{35}
\]
For the second bound use \(\sin(2\pi t)\le1/\sqrt2<3/4\)
and \(a>3/2\). Put \(R=|D|^2\) and
\(\sigma=\sqrt{1-b^2}>4/5\). The exact equation
\(|D^2-1|^2=4\) gives
\[
                  (R-1)^2+4b^2=4,\qquad R-1=2\sigma.
 \tag{36}
\]
The positive sign is forced by \(R>1\).
Differentiating \(D\) on the original branch gives
\(D'=\pi i(D-D^{-1})\). Consequently
\[
 f''(t)=-\frac{b'}{1-b^2}
       =-\frac{2\pi\,\Re(D^{-1})}{\sigma}>-\frac{5\pi}{3}.
 \tag{37}
\]
Indeed \(\Re(D^{-1})\le1/|D|<2/3\).
Since \(f'(1/2)=0\) and \(f(1/2)=\lambda_*\), integration
over length \(1/8\) gives
\[
                  \lambda(3/8)>
                       \lambda_*-\frac{5\pi}{384}-J(3/8).
 \tag{38}
\]

Set \(j_8=-J(3/8)\). Monotonicity of the sine on
\([3/8,1/2]\) proves
\[
 j_8\ge\frac18\log(2\sin(3\pi/8))
          >\frac18\log(11/6)>\frac5{68}.
 \tag{39}
\]
Here \(2\sin(3\pi/8)=\sqrt{2+\sqrt2}>11/6\), since
\(2401<2592\) proves \(\sqrt2>49/36\), and
\(\log(11/6)>10/17\).
At the real trial point,
\[
 \Re\Psi(3/8,1/4)=\lambda(3/8)+2j_8+b_2/4.
 \tag{40}
\]
The equality uses \(J(5/8)=-J(3/8)\) and the original
purely imaginary real-point chirps.

Now move only \(e=3/8+i\eta\) from \(\eta=0\) to
\(\eta=h_e\). The entire segment belongs to the
[original endpoint rectangle](research_mixed_endpoint_cap_rectangle.md).
Its original unsquared critical point obeys
\[
 \Re u_c>17/100,\qquad \Im u_c>0,\qquad
                           0<\Re(e-u_c)<1/2.
 \tag{41}
\]
The exact derivative
\(S'(e)=-J'(e-u_c)+i\pi u_c\) therefore has
\(\Im S'(e)>17\pi/100\). At nonpositive \(\eta\), the
original disk arguments give
\[
 \Im g'(5/8+i\eta)\ge-\pi/8,\qquad
 \Im g'(3/8+i\eta)\le\pi/8.
 \tag{42}
\]
The derivative of the last chirp in \(\Psi\) has imaginary
part \(-\pi/8\). Thus
\[
               \Im\Psi_e(3/8+i\eta,1/4)>
                     \frac{17\pi}{100}-\frac{3\pi}{8}
                         =-\frac{41\pi}{200}.
 \tag{43}
\]
The downward real-rate cost is at most
\[
                     \frac{51}{1000}\frac{41\pi}{200}
                            =\frac{2091\pi}{200000}.
 \tag{44}
\]

Finally raise the incoming target from \(1/4\) to \(1/4+iH\)
while keeping this private point fixed. In
\(\Psi_a=g'(e+a)-g'(a)\), the first logarithm has real
argument coordinate \(5/8\) and negative imaginary part
as a logarithm; the second has coordinate \(1/4\) and
positive imaginary part. Both are the original strip logarithms.
Hence \(-\Im\Psi_a>0\): this raise only increases the real
cap rate. Combining (38)--(44) proves
\[
 \Re\Psi(3/8+ih_e,1/4+iH)>
       \lambda_*+3j_8+\frac{b_2}{4}
                    -\pi\left(\frac5{384}+\frac{2091}{200000}\right).
 \tag{45}
\]
This is a trial inside the original cap main profile. Neither
cap noncancellation nor a lower estimate for a finite coefficient
has entered.

## 5. Summation of the original trial rates

Use (22), (24), \(\Delta_\beta>0\), the two copies of (9),
and the cap bound (45). Since
\(A_H\ge b_2/4+\pi H/4\), their sum gives
\[
 T_0>
 \frac32\lambda_*+2b_2+3j_8-\pi C,
 \qquad
 T_1>
 2\lambda_*+\frac32b_2+3j_8-\pi C,
 \tag{46}
\]
where
\[
 C=\frac5{384}+\frac{2091}{200000}+\frac{15H}{4}
   =\frac{97}{1920}+\frac{2091}{200000}<\frac{61}{1000}.
 \tag{47}
\]
The final cross-product comparison in (47) is
\(19400000<19409280\). This accounts for both full
selected factorial alternatives and their two monomial costs.

For \(\beta=0\), insert (13), (39), and \(\pi<22/7\):
\[
\begin{split}
 T_0&>
 \frac{231}{200}+\frac{23}{20}+\frac{15}{68}
                      -\frac{671}{3500}\\
 &=\frac{277731}{119000}
   =\frac73+\frac{193}{357000}>\frac73.
\end{split}
\tag{48}
\]
For \(\beta=1\), the same rational witnesses improve the
first two terms by \(39/400\), so the same strict lower
bound holds. Equation (11) now proves (1), with additional
spare reserve from the original \(1/100\) profile gap.

This conclusion is uniform over the actual third real plateau
and both canonical following types. It depends on the original
coupled-reference calibration in (11), even though the new
lower estimates used the stated enclosing height bounds.
There has been no replacement of the affine constant by an
uncalibrated positive envelope.

For clarity about the intended seam comparison, the following
is an elementary scalar consequence, not a finite-source
assertion:
\[
 \frac73-\left\{\frac{433}{500}
                  +\frac{39}{80}+\frac7{15}
                  +\frac{1271}{2500}\right\}
     =\frac{143}{30000}>\frac1{250}.
 \tag{49}
\]
Thus a complete seam source bounded by the expression in braces,
with the same outgoing half allocation, has room for a positive
collar allowance. Establishing that finite seam bound, including
the complete \(f_{44,N}\) and both second Fourier alternatives,
is a separate task. This note itself is only the calibrated
action-floor theorem.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_double_selected_tangent_completion.md | ad2012d03f5022abbb593ab3c80659b8b778a6d55fedf980c7d4ead2eb7726b8 |
| research_mixed_complete44_second_selected_real_first_arc.md | f9a9a53a68faf11293f8463e713afdb951ffd5cddcf18e8f1dee4d09ff5fb37c |
| research_mixed_symmetric_closing_complete_column_norm.md | 4df2375a3ae9340b0137effb2d8193eed4a3ed090a0c1bde58fb9c434f3fe519 |
| research_mixed_endpoint_cap_rectangle.md | 9211d45bdd031c908690a723ebcd4b40a34fed90f44858301a809ee5901c15e8 |
| research_mixed_retained_prefix_unselected_plateau.md | 4f8be2ee4fd0aceda28ad4d96bb4b57d864765438183563c34db070823d6d72b |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |

Author full proof readback and all six direct-source implication reads
are complete; the six source hashes have been checked. Independent
full proof and direct-source review is required before adoption.
No mathematical numerical evaluation, saved-value arithmetic, test,
import, compilation or frozen-source edit is used.
