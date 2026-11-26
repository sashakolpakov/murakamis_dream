# The all-power characteristic action and its sharp monotone ceiling

Private written proof, 16 November 2026.

The integrated dominant terminal characteristic equals the selected
unit-charge stationary action of the original edge phase. This
identity includes the endpoint action constant and uses the signed
root convention already fixed for the original physical operator.
It yields a strictly increasing sequence of actions, bounded sharply
by the complete-edge constant, with an explicit large-power deficit.
It does not prove that the dominant source coefficient survives,
identify an arbitrary filled volume, or pay the mixed-source cost
of a larger parent graph.

The selected leaf stationary point and its original phase were
already established in research_terminal_powers_three_and_above.md.
For power two, the complete boundary-path calibration, including
its \(i\pi/2\) action correction, is in §8 of
research_two_crossing_terminal_filling.md. The new assertions here
are the all-power identification with the dominant characteristic
integral, its strict monotonicity, and its sharp limiting deficit.

## 1. Characteristic normalization and an elementary ceiling

Let \(n\ne0\), \(m=|n|\), and let \(\rho_m(v)\) be the largest
selected physical shift modulus in the adopted ordering theorem.
The row coordinate is \(v=j/N\), increasing from \(0\) to \(1/2\);
the leading physical color is \(2\cos(2\pi v)\). Define
\[
                  \mathcal I_n=\mathcal I_m
                    :=\int_0^{1/2}\log\rho_m(v)\,dv.
 \tag{1}
\]
The signed moduli agree. For \(m=1\), \(\rho_m=1\) and
\(\mathcal I_m=0\).
For \(m\ge2\), use
\[
 h=\sin(\pi v),\qquad
 a=\frac{h^2}{1-h^2},\qquad
 p_m(\zeta)=\zeta U_{m-1}(\zeta).
 \tag{2}
\]
The dominant first-quadrant root \(\zeta_m(h)\) satisfies
\[
 p_m(\zeta_m)=ih,\qquad
 \log\rho_m(v)=
           2\operatorname{Re}\operatorname{asinh}
                              (\zeta_m(h)/\sqrt a).
 \tag{3}
\]
For \(m\ge3\), it is the branch issuing from
\(\zeta_m(0)=\cos(\pi/m)\). For \(m=2\),
\[
                \zeta_2(h)=e^{i\pi/4}\sqrt{h/2}.
 \tag{4}
\]
These are precisely the dominant labels of the ordering theorem.
To check the sign in (3), at the first positive root
\[
 p_m'(\cos(\pi/m))
             =\frac{m\cos(\pi/m)}{\sin^2(\pi/m)}>0
                       \quad(m\ge3).
\]
Thus its first-quadrant continuation has value \(ih\).
This sign cannot change for \(h>0\).
Equation (4) gives the same sign for \(m=2\).

Put
\[
 G=\sum_{k\ge0}\frac{(-1)^k}{(2k+1)^2}
     =\int_0^{\pi/4}\log\cot s\,ds,\qquad
 M_\infty=\frac{4G}{\pi}.
 \tag{5}
\]
For example, substituting \(u=\tan s\) in the integral
gives \(-\int_0^1\log u/(1+u^2)\,du\); the finite geometric
series and dominated convergence give the displayed sum.

**Proposition 1.** For every \(m\ge2\),
\[
 0<\log\rho_m(v)<2\operatorname{asinh}(\cot(\pi v))
                         \quad(0<v<1/2),
 \qquad 0<\mathcal I_m<M_\infty .
 \tag{6}
\]

*Proof.* The symmetric real-root factorization of
\(p_m=\zeta U_{m-1}\) shows that for \(|\zeta|\ge1\),
\[
 |p_m(\zeta)|\ge p_m(|\zeta|)\ge p_m(1)=m.
 \tag{7}
\]
Indeed each symmetric root factor obeys
\(|\zeta^2-r^2|\ge|\zeta|^2-r^2\), where \(0<r<1\);
the one or two zero factors obey the same radial comparison.
Since \(|p_m(\zeta_m)|=h<1\), one has \(|\zeta_m|<1\).
Write \(\zeta_m=\sqrt a\,\sinh(R+i\theta)\), with
\(R>0\), \(0<\theta<\pi/2\), as in the ordering theorem.
Then
\[
       |\zeta_m|^2=a\sinh^2R+a\sin^2\theta<1.
\]
Consequently \(2R<2\operatorname{asinh}(a^{-1/2})\),
which is the pointwise inequality in (6).
The dominating function is integrable:
\[
 \int_0^{1/2}2\operatorname{asinh}(\cot(\pi v))\,dv
       =\frac4\pi\int_0^{\pi/4}\log\cot s\,ds=M_\infty .
 \tag{8}
\]
Here \(\operatorname{asinh}(\cot w)=\log\cot(w/2)\)
for \(0<w<\pi/2\). Positivity and strictness on every
interior interval prove (6). \(\square\)

## 2. A specified continuation of the original edge phase

Let the external angle \(u\) be real, \(0\le u<\pi\), and let
\[
 {\cal D}=\{t:0<\operatorname{Re}t<\pi,\
                       \operatorname{Im}t<0\}.
\]
The branches below extend to the adjacent real segment and to
the origin. Write
\[
 r_t(t,u)=\operatorname{asinh}(\cos(u/2)\tan(t/2)),\qquad
 r_u(t,u)=\operatorname{asinh}(\cos(t/2)\tan(u/2)).
 \tag{9}
\]
Use the principal inverse hyperbolic sine. If
\(t/2=A-iB\), \(0<A<\pi/2\), \(B>0\), then \(\tan(t/2)\)
is in the fourth quadrant and \(\cos(t/2)\) is in the first.
Thus these branches are regular on the stated domain.
Define the edge phase there by
\[
 \begin{split}
 \psi(t,u)={}&M_\infty
   -\frac1\pi\int_0^u\operatorname{asinh}(\tan(s/2))\,ds\\
   &-\frac1\pi\int_0^t
              \operatorname{asinh}(\cos(u/2)\tan(z/2))\,dz .
 \end{split}
 \tag{10}
\]
The second integral is path independent in the right lower
strip with the origin attached. This specifies the original
edge-phase continuation, not just its real part.

The two differential formulas are
\[
                         \psi_t=-r_t/\pi,\qquad
                         \psi_u=-r_u/\pi .
 \tag{11}
\]
To verify the second, put \(h=\cos(u/2)\) and
\[
       D=h^2+(1-h^2)\cos^2(t/2).
\]
For \(0<h<1\), \(D\) has positive imaginary part on
\({\cal D}\). Its principal square root gives, with the
branches in (9),
\[
 \partial_u r_t=\partial_t r_u
       =-\frac{\sin(u/2)\sin(t/2)}{2\sqrt D}.
 \tag{12}
\]
Indeed
\(\sqrt{1+h^2\tan^2(t/2)}=\sqrt D/\cos(t/2)\) and
\(\sqrt{1+\tan^2(u/2)\cos^2(t/2)}=\sqrt D/h\);
their arguments agree with the principal square roots.
The formulas extend to \(u=0\).
Integrating (12) from \(t=0\), where
\(r_u(0,u)=\operatorname{asinh}(\tan(u/2))\), proves (11).
The derivatives and the normalization \(\psi(0,0)=M_\infty\)
are those of the original phase in the pinned sources.

Also
\[
 \int_0^\pi\operatorname{asinh}(\tan(s/2))\,ds=4G,
                 \qquad \lim_{u\uparrow\pi}\psi(0,u)=0.
 \tag{13}
\]
This is the same integral as (8), after reflection of its
angle variable. No additive real constant is left unspecified.

## 3. The dominant characteristic follows the unit primitive

For integer \(m\ge2\), now put
\[
 h=\cos(u/2),\qquad
 \theta_m(h)=\arccos\zeta_m(h)=A-iB,\qquad
 t_m(u)=2\theta_m(h).
 \tag{14}
\]
The inverse cosine is the branch with
\(0<A<\pi/2\), \(B>0\). This branch exists throughout
\(0<h\le1\), since \(\zeta_m\) is in the first quadrant.
Equation (3) is equivalent to
\[
                        \sin(m\theta_m)=ih\tan\theta_m.
 \tag{15}
\]
There is no division by a zero sine in this equivalence on
the indicated strip.

**Lemma 2.** The branch in (14) obeys the original unit-charge
stationary equation, with its primitive lift:
\[
          r_t(t_m(u),u)=im\theta_m-i\pi,
 \qquad
          \partial_t\left[\psi(t,u)+\frac{im}{4\pi}t^2-it\right]
                            _{t=t_m(u)}=0 .
 \tag{16}
\]

*Proof.* The real and imaginary parts of (15) are both
strictly positive. More explicitly,
\[
 \sin(mA)\cosh(mB)
      =\frac{h\sinh(2B)}{\cos(2A)+\cosh(2B)}>0,
\]
\[
 -\cos(mA)\sinh(mB)
      =\frac{h\sin(2A)}{\cos(2A)+\cosh(2B)}>0.
 \tag{17}
\]
Thus \(mA\) belongs to one of the disjoint intervals
\((\pi/2+2k\pi,\pi+2k\pi)\).
As \(h\downarrow0\), the dominant label gives
\(\theta_m\to\pi/m\) for \(m\ge3\), and
\(\theta_2\to\pi/2\) for \(m=2\).
Continuity in (17) therefore fixes \(k=0\) throughout:
\[
                           \pi/2<mA<\pi.
 \tag{18}
\]
The number \(im\theta_m-i\pi\) has positive real part
and imaginary part in \((-\pi/2,0)\), and its hyperbolic
sine is \(h\tan\theta_m\), by (15).
The hyperbolic sine is one-to-one from that half-strip
onto the fourth quadrant. Its inverse is the principal
branch used in (9). This proves the first equation in (16).
The second follows by substituting it in (11). \(\square\)

Define the stationary action
\[
 S_m(u)=\psi(t_m(u),u)+\frac{im}{4\pi}t_m(u)^2-it_m(u).
 \tag{19}
\]
Its derivative is exactly
\[
 S_m'(u)=-\frac1\pi r_u(t_m(u),u)
        =-\frac1\pi\operatorname{asinh}
                                (\zeta_m(h)\tan(u/2)).
 \tag{20}
\]
Stationarity removes the derivative of \(t_m\).
This is an identity of the stated phase branches; it does
not require positivity of every intermediate cell.

**Lemma 3.** The endpoint action, including its imaginary
constant, is
\[
                          \lim_{u\uparrow\pi}S_m(u)
                                     =-\frac{i\pi}{m}.
 \tag{21}
\]

*Proof.* For \(m\ge3\), \(t_m(u)\to2\pi/m<\pi\).
The second integral in (10) tends to zero uniformly on a
fixed compact path, since its integrand tends to zero.
Equation (13) gives \(\psi(t_m(u),u)\to0\).
Substitution in the remaining two terms of (19) gives (21).

For \(m=2\), use (4):
\[
 \theta_2=\frac\pi2-e^{i\pi/4}\sqrt{h/2}+O(h^{3/2}).
 \tag{22}
\]
Thus \(\pi/2-A\asymp\sqrt h\), \(B=O(\sqrt h)\).
Integrate the second term of (10) first along
\([0,2A]\), then vertically to \(2A-2iB\).
On the real segment, \(\operatorname{asinh}x\le x\) for
\(x\ge0\), so
\[
 \int_0^{2A}|\operatorname{asinh}(h\tan(s/2))|\,ds
                  \le-2h\log\cos A=O(h\log(1/h)).
 \tag{23}
\]
On the vertical segment, \(|\cos(s/2)|\ge\cos A\asymp\sqrt h\),
while \(\sin(s/2)\) is bounded. Hence the inverse-hyperbolic-sine
argument is \(O(\sqrt h)\); its integral over a segment of
length \(O(\sqrt h)\) is \(O(h)\).
Again \(\psi(t_2(u),u)\to0\), while \(t_2(u)\to\pi\).
The remaining terms tend to \(-i\pi/2\), proving (21)
also in this case. \(\square\)

## 4. Exact action calibration

**Theorem 4.** For every integer \(m\ge2\),
\[
 \boxed{\quad
 \mathcal I_m
   =\operatorname{Re}\left[
       \psi(t_m(0),0)+\frac{im}{4\pi}t_m(0)^2-it_m(0)
                      \right].\quad}
 \tag{24}
\]
The saddle on the right is exactly the selected unit-charge
leaf saddle in the original phase. The same real value
applies to negative powers by reflection.

*Proof.* Substitute \(u=\pi-2\pi v\) in (20).
Then \(h=\sin(\pi v)\) and
\[
 \tan(u/2)=\cot(\pi v)=a^{-1/2}.
 \]
Equations (3) and (20) give
\[
              \frac d{dv}\operatorname{Re}S_m(\pi-2\pi v)
                           =\log\rho_m(v).
 \tag{25}
\]
The endpoint constant in (21) has real part zero.
Integrating from \(v=0\) to \(v=1/2\) proves (24).
The integral converges by (6), or by the endpoint estimates
of the ordering theorem.
At the full complex-action level, the retained constant is
\[
 S_m(0)+\frac{i\pi}{m}
   =\int_0^{1/2}2\operatorname{asinh}
                  (\zeta_m(\sin\pi v)\cot(\pi v))\,dv.
 \tag{26}
\]
Here the imaginary integral is also convergent, since the
chosen inverse-hyperbolic-sine imaginary part lies in
\((0,\pi/2)\).
Formula (26) is a phase identity, not a change of a finite
crossing carrier.

At \(u=0\), (16) is the original unit primitive. The
uniqueness argument below identifies this point with the
archived selected saddle, without selecting merely a root
of an exponentiated equation. Reflection
\(t\mapsto-\bar t\), with the reflected phase branch,
conjugates the signed action and leaves its real part
unchanged. This agrees with \(\mathcal I_{-m}=\mathcal I_m\).
\(\square\)

For \(m=2\), this calibration recovers the exact constant
\[
                         \mathcal I_2=M_\infty/2=2G/\pi.
 \tag{26a}
\]
Indeed (4), with \(s=\sin(u/2)\), gives
\[
 \operatorname{asinh}(\zeta_2(h)\tan(u/2))
       =\tfrac12\operatorname{artanh}s+iu/4.
\]
Taking the hyperbolic sine verifies the identity:
both real and imaginary parts are \(s/(2\sqrt h)\);
the displayed imaginary part fixes the principal branch.
Now integrate its real part using
\(\operatorname{artanh}(\sin(u/2))
 =\operatorname{asinh}(\tan(u/2))\) and (13).
This is the same normalization as the earlier two-crossing
calibration.

## 5. Real-power continuation, strict increase, and sharp deficit

A real parameter \(p\ge2\) is useful for comparing these
classical actions. This continuation is a phase parameter;
no new convention for a finite quantum power is needed.

**Lemma 5.** For every real \(p\ge2\), there is exactly one
selected saddle \(t_p=2A_p-2iB_p\) with
\(0<A_p<\pi/2\), \(B_p>0\), satisfying
\[
                 \operatorname{asinh}(\tan(t_p/2))
                               =ip\,t_p/2-i\pi.
 \tag{27}
\]
It is real analytic in \(p\).

*Proof.* On the indicated strip the exact identity is
\[
 \operatorname{asinh}(\tan(A-iB))
 =\operatorname{artanh}\frac{\sin A}{\cosh B}
     -i\arctan\frac{\sinh B}{\cos A}.
 \tag{28}
\]
It follows, for example, by taking the logarithm of
\(\sec(A-iB)+\tan(A-iB)\), whose real part is positive.
Thus (27) is equivalent to
\[
 \sin A=\cosh B\,\tanh(pB),\qquad
 pA+\arctan\frac{\sinh B}{\cos A}=\pi.
 \tag{29}
\]
For every fixed real \(p>0\), the first right side increases
strictly from zero to infinity as \(B\) increases.
It defines a strictly increasing function \(B=B_p(A)\).
The left side of the second equation then increases
strictly from zero, as \(A\downarrow0\), to
\((p+1)\pi/2\), as \(A\uparrow\pi/2\).
For \(p\ge2\), the target \(\pi\) lies strictly between
these endpoints. Existence and uniqueness follow.
No step of this argument uses integrality of \(p\).

The stationary Hessian is
\[
 \partial_t^2\left(\psi(t,0)+\frac{ip}{4\pi}t^2-it\right)
                      =\frac{-\sec(t/2)+ip}{2\pi}.
 \tag{30}
\]
Its real part is negative on the right lower strip,
since \(\operatorname{Re}\sec(t/2)>0\).
It is therefore nonzero. The holomorphic implicit function
theorem locally in \(p\), and uniqueness, give the stated
real-analytic continuation. \(\square\)

Let
\[
             M(p)=\operatorname{Re}\left[
               \psi(t_p,0)+\frac{ip}{4\pi}t_p^2-it_p\right].
 \tag{31}
\]

**Theorem 6.** The actions satisfy
\[
 \mathcal I_1=0<\mathcal I_2<\mathcal I_3<\cdots<M_\infty,
 \qquad \lim_{m\to\infty}\mathcal I_m=M_\infty,
 \tag{32}
\]
and more precisely
\[
 \boxed{\qquad
 \mathcal I_m=M_\infty-\frac{\pi}{m^2}+O(m^{-4})
                                      \quad(m\to\infty).
 \qquad}
 \tag{33}
\]
The real continuation has the exact positive derivative
and deficit formulas
\[
 M'(p)=\frac{2A_pB_p}{\pi}>0,\qquad
 M_\infty-M(p)=\int_p^\infty\frac{2A_sB_s}{\pi}\,ds.
 \tag{34}
\]

*Proof.* Stationarity removes \(t_p'\) on differentiating
(31), giving
\[
 M'(p)=\operatorname{Re}\frac{i t_p^2}{4\pi}
                             =\frac{2A_pB_p}{\pi}>0.
 \tag{35}
\]
Also (29) implies \(A_p<\pi/p\). For sufficiently large
\(p\),
\[
 \tanh(pB_p)\le\sin A_p\le\pi/p,\qquad
                B_p\le p^{-1}\operatorname{artanh}(\pi/p)
                            =O(p^{-2}).
 \tag{36}
\]
Thus \(t_p\to0\), and the real parts of both remaining
terms in (31) tend to zero. The phase tends to
\(\psi(0,0)=M_\infty\). Therefore \(M(p)\uparrow M_\infty\).
Together with (24) and Proposition 1 this gives (32)
and the positive integral in (34).

For its sharp asymptotic, put \(z=1/p\), \(t_p=zT(z)\).
Near the origin,
\[
 r(t):=\operatorname{asinh}(\tan(t/2))
                           =t/2+t^3/48+O(t^5).
 \tag{37}
\]
Equation (27) becomes
\[
                         T=2\pi-2i\,r(zT).
 \tag{38}
\]
At \(z=0,T=2\pi\), the derivative with respect to \(T\)
of this implicit equation is a unit.
It defines a holomorphic \(T(z)\).
The estimates (36) and (27) identify the selected real
branch with this implicit solution for large \(p\).
Using (37) in (38) yields
\[
        t_p=\frac{2\pi}{p+i}+O(p^{-4}),
 \quad
        A_p=\frac{\pi}{p}+O(p^{-3}),
 \quad
        B_p=\frac{\pi}{p^2}+O(p^{-4}).
 \tag{39}
\]
For the last two estimates, expand the displayed rational
term; its order-\(p^{-3}\) coefficient is real.
Hence
\[
                         M'(p)=2\pi p^{-3}+O(p^{-5}).
 \tag{40}
\]
Integrating (40) in (34) proves (33). \(\square\)

The elementary ceiling in §1 and the stationary-action
calibration in §§2--4 are logically separate proofs of
different statements. The latter fixes an original
primitive phase branch, including its imaginary endpoint
constant. It does not assert that the entire boundary
continuation is a positive ideal-cell subdivision or a
family of completed marked cone metrics. Any volume
identification needs its own geometric marking theorem.
Likewise (32)--(34) do not compare the terminal cost with
the available energy of an arbitrary parent or control
the retained mixed forcing after ordinary branching.

## 6. Direct-source readbacks

The complete direct sources were read at their stated
unchanged versions, and the used implications and hashes checked:

* [Global terminal modulus ordering](research_terminal_twist_global_modulus_order.md),
  SHA256
  79f26184f1ea0a4d45bb9961397175fc1fa6bad332482edd681a85156a6eae3a.
  Its full author readback is retained; the exact dominant
  label, signed convention, and ellipse formula were rechecked.
* [Selected stationary geometry for powers at least three](research_terminal_powers_three_and_above.md),
  SHA256
  393618c7de5f9a2d8f0c816b568abf97f63419cd834cf7b56eccbb300fd608cd.
  Its complete text was freshly read. The extension to real
  \(p\ge2\) is proved above, not inferred from an integer assertion.
* [Original two-crossing terminal source and phase](research_two_crossing_terminal_filling.md),
  SHA256
  7aedaded3efa3058a3250b2120cc4f41bcad1f7f20aff2e7f4dd4fab19aae9ed.
  The prior complete terminal-source readback is retained at
  the verified unchanged pin; its phase normalization and
  full §8 boundary calibration were reread.

All new phase-domain, branch, endpoint, derivative, and
integral-normalization arguments are given above.
Only written mathematics, source text and hashes were used.
No mathematical program, numerical experiment, test or build
was run. Frozen notes and public manuscripts are unchanged.
