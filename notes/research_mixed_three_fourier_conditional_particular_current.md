# An exact particular current for the twice-crossed conditional source

Research deduction, 7 November 2026. A third-order periodic contour
kernel isolates an exact particular solution of the incoming
difference equation for the literal \(C_0\) source. Its full
cyclotomic forcing factors are retained. A uniform polynomial
bound and two Cauchy estimates determine the signed current,
including all fixed parameter derivatives.

After restoration of the original crossing scalar, its leading
term is the already identified first-channel observation after
two negative crossings. The difference between the complete
source and this particular current satisfies the homogeneous
second-order equation exactly. No dominance of that homogeneous
contribution, or full twice-crossed asymptotic, is asserted.
No numerical evaluation is used.

## 1. The original row and an exact telescoper

Put
\[
 r=e^{-2\pi i/N},\quad P_j=(r;r)_j,\quad
 X=e^{-2\pi ia},\quad W=e^{-2\pi iy},
\]
and use the literal sum
\[
 F_N(X,W)=C_{0,N}(X,W)
     =\sum_{j=0}^{N-1}\frac{X^{-j}(rX;r)_j(rW;r)_j}{P_j^2}.
\tag{1}
\]
The original factorial interpolation is
\[
 T_N(s;a,y)=e^{2\pi iNas}
       \Pi_N(s+a)\Pi_N(s+y)E_N(a)E_N(y)E_N(s)^2.
\tag{2}
\]
Its physical values are exactly the summands in (1), including
index zero. We use the global holomorphic factorial chart of
[the endpoint-current theorem](research_mixed_three_fourier_conditional_endpoint_current.md),
without resetting shifted numerator factors at a positive wall.

The parameters range over compact subsets of
\[
 \mathcal D=\{\,0<\Re a<1/2,\quad 0<\Re y<1/2,\quad
                                                  \Im y>0\,\}.
\tag{3}
\]
All exact current identities below hold for sufficiently large
\(N\), with the threshold uniform on each such compact set.
The threshold ensures that the finitely many incoming shifts
remain in an admitted open parameter domain and that the
horizontal connectors at infinite height decay.

Write \(\mathsf T_X f(X)=f(rX)\) and
\(\mathsf D=(1-rX)\mathsf T_X+rX\).
The original ordered operator is
\[
 \mathcal L_{N,W}
 =(1-r^{-2}X^{-1})\mathsf D^2
       +(r^{-1}-2+Wr^{-1}X^{-1})\mathsf D+1-W.
\tag{4}
\]
Its exact finite-source equation is
\[
 \mathcal L_{N,W}F_N
        =-\frac{(1-W^N)(X^{-N}-1)}{N^2},
\tag{5}
\]
as proved in
[the conditional difference equation](research_mixed_three_fourier_conditional_difference_equation.md).

**Lemma 1.** With \(U=e^{-2\pi is}\), the original row satisfies
\[
 \mathsf D\,T_N(s)=U^{-1}T_N(s),\qquad
 \mathcal L_{N,W}T_N(s)=B_N(s)-B_N(s+1/N),
\tag{6}
\]
where
\[
                         B_N(s)=(e^{2\pi is}-1)^2T_N(s).
\tag{7}
\]
These are exact identities of the original interpolation.

*Proof.* Its two one-step relations are
\[
 \frac{T_N(s;a+1/N,y)}{T_N(s;a,y)}
       =\frac{U^{-1}(1-rXU)}{1-rX},
 \qquad
 \frac{T_N(s+1/N)}{T_N(s)}
       =\frac{X^{-1}(1-rXU)(1-rWU)}{(1-rU)^2}.
\tag{8}
\]
They follow from the factorial recurrence, with the original
chirp retained. The first proves \(\mathsf DT_N=U^{-1}T_N\).
The second gives
\[
 \frac{B_N(s+1/N)}{T_N(s)}
   =r^{-2}X^{-1}U^{-2}
       -r^{-1}(1+WX^{-1})U^{-1}+W.
\]
Subtracting this from
\(B_N(s)/T_N(s)=U^{-2}-2U^{-1}+1\) gives (4)
applied to \(T_N\). Written without the temporary quotients,
the identities extend across every numerator zero. \(\square\)

In particular the real zero-mode integral is not automatically
homogeneous. If \(I_N=N\int_{\alpha_N}^{\beta_N}T_N(s)\,ds\),
then its telescoper leaves the two short boundary integrals
\[
 \mathcal L_{N,W}I_N
   =N\left\{\int_{\alpha_N}^{\alpha_N+1/N}B_N(s)\,ds
           -\int_{\beta_N}^{\beta_N+1/N}B_N(s)\,ds\right\}.
\tag{9}
\]
The apparent pole of \(B_N\) at \(s=1\) is removable: its
quadratic prefactor cancels the squared factorial pole there.
Equation (9) retains these terms instead of identifying the
whole zero mode with a selected homogeneous state.

## 2. A contour particular solution with the full forcing

Let \(\alpha_N=-1/(2N)\), set \(t=e^{-2\pi iNs}\), and define
the \(1/N\)-periodic meromorphic kernel
\[
                         k_{3,N}(s)=\frac{t(1+t)}{(1-t)^3}.
\tag{10}
\]
Its contour in the following integral is oriented upward:
\[
 \mathcal I_{3,N}(a,y)
       =\int_{\alpha_N-i\infty}^{\alpha_N+i\infty}
                         k_{3,N}(s)T_N(s;a,y)\,ds,\qquad
 A_N(a,y)=\frac{N^3}{2}\mathcal I_{3,N}(a,y).
\tag{11}
\]
The function \(A_N\) is defined by the integral, even when
\(X^N=1\). It is not obtained by dividing a finite-source zero.

**Lemma 2.** The integral in (11) converges absolutely and is
holomorphic on the admitted parameter domains. Uniformly on
compact subsets of (3),
\[
                 |\mathcal I_{3,N}|\le CN^{-2},\qquad
                 |A_N|\le CN.
\tag{12}
\]
Moreover its exact equation is
\[
                         \mathcal L_{N,W}A_N=-1.
\tag{13}
\]

*Proof of the bound.* On \(s=\alpha_N+iv\), write
\(T=e^{2\pi Nv}>0\), so \(t=-T\). The exact midpoint estimate
from the endpoint-current theorem is
\[
 |T_N(\alpha_N+iv)|
        \le \frac{C}{N}(1+T)e^{NL(v)}
\tag{14}
\]
on any fixed height interval, where
\[
 L(v)=\Re\{g(a+iv)+g(y+iv)-g(a)-g(y)\}
                                         -2\pi(\Re a)v,
\]
\[
 L(0)=0,\qquad
 -2\pi(1-\Re y)<L'(v)<-2\pi\Re a.
\tag{15}
\]
The kernel satisfies
\[
 |k_{3,N}(\alpha_N+iv)|
       =\frac{T|1-T|}{(1+T)^3}
       \le\frac{T}{(1+T)^2}.
\tag{16}
\]
Thus the product in (14) has rate at most \(L(v)+2\pi v\)
for \(v\le0\), and at most \(L(v)\) for \(v\ge0\).
It is bounded by \(-2\pi d|v|\), with any common lower
bound \(d>0\) for \(\Re a,\Re y\) on the compact set.
Its compact-height integral is \(O(N^{-2})\).

This estimate also includes the entire unbounded tails.
Indeed the exact regrouped weight
\[
 w_{N,0}(v)=\frac1{1+e^{2\pi Nv}}
                                      -\boldsymbol1_{\{v<0\}}
\]
satisfies
\[
             |k_{3,N}(\alpha_N+iv)|\le |w_{N,0}(v)|
                           \quad(v\ne0).
\tag{17}
\]
The left-side tail estimates (23)--(25) in the endpoint-current
proof control \(\int |w_{N,0}(v)T_N(\alpha_N+iv)|\,dv\)
by \(CN^{-2}\), with zero forcing exponent on this left side.
Those estimates use the explicit cyclotomic remainder and a
fixed cutoff height before taking \(N\) large. They are not
an inference from fixed-level convergence. Equations (16)--(17)
therefore prove (12) and provide compact-uniform integrable
majorants for holomorphy. The value at \(v=0\) is harmless.

*Proof of the exact equation.* Apply (6) under the integral.
The kernel is \(1/N\)-periodic, so shifting the second
vertical line gives
\[
 \mathcal L_{N,W}\mathcal I_{3,N}
  =\int_{\alpha_N-i\infty}^{\alpha_N+i\infty} k_{3,N}B_N\,ds
    -\int_{\alpha_N+1/N-i\infty}^{\alpha_N+1/N+i\infty}
                                                    k_{3,N}B_N\,ds.
\tag{18}
\]
The original factorial asymptotics at infinite height give
decay \(e^{-2\pi N(1-\Re y)H}\) at the upper horizontal
connector. At the lower connector the factor in (7) contributes
\(e^{4\pi H}\), so its decay is
\[
                   e^{-2\pi\{N(1-\Re a)-2\}H}.
\tag{19}
\]
For sufficiently large \(N\) this is strict uniformly on
the parameter compact. The constants are those of the
original fixed-level factorial interpolation; they are not
needed to be uniform in \(N\) for this exact contour shift.

There is just one kernel pole in the strip, at \(s=0\).
The factorial factors in \(B_N\) are holomorphic there and
\(T_N(0)=1\). Consequently
\[
 k_{3,N}(s)=\frac{2}{(2\pi iNs)^3}+O(s^{-2}),\qquad
 B_N(s)=(2\pi is)^2+O(s^3),
\]
\[
             \operatorname{Res}_{s=0}(k_{3,N}B_N)
                             =\frac1{\pi iN^3}.
\tag{20}
\]
Left-up minus right-up has clockwise orientation, so (18)
equals \(-2/N^3\). Multiplying by \(N^3/2\) proves (13).
All factor zeros and all finite \(N\)-phases have remained
in this residue calculation. \(\square\)

Define
\[
 \boxed{\quad
 F_N^{\rm part}(X,W)=
       \frac{(1-W^N)(X^{-N}-1)}{N^2}A_N(a,y),\qquad
 F_N^{\rm hom}=F_N-F_N^{\rm part}.
 \quad}
\tag{21}
\]
The two displayed cyclotomic factors are invariant under
\(a\mapsto a+1/N\); they commute with every term of (4).
Equations (5), (13) therefore give the exact decomposition
\[
 \boxed{\quad
 \mathcal L_{N,W}F_N^{\rm part}
       =-\frac{(1-W^N)(X^{-N}-1)}{N^2},\qquad
 \mathcal L_{N,W}F_N^{\rm hom}=0.
 \quad}
\tag{22}
\]
These identities hold through every physical incoming zero
lying in the admitted parameter domain.
The functions in (21) are not separately claimed to belong
to the original finite Laurent band, so (22) does not
contradict uniqueness within that band.

## 3. The signed particular-current packet

**Theorem 3.** Uniformly on compact subsets of \(\mathcal D\),
\[
 \boxed{\quad
 A_N(a,y)=-\frac1{(W-1)(X^{-1}-1)}+O(N^{-1}).
 \quad}
\tag{23}
\]
The error is holomorphic and has order \(O(N^{-1})\) with
every fixed parameter derivative on smaller compact sets.

*Proof.* The exact constant-shift coefficient of (4) is
\[
 \sigma_N=\mathcal L_{N,W}1
              =(r^{-1}-W)(1-r^{-1}X^{-1}).
\tag{24}
\]
It has a uniform positive modulus on every fixed parameter
compact for all sufficiently large \(N\):
\(|W|>1\) and \(X\ne1\) there.
Expand (4) as a second-order operator in the shift
\(a\mapsto a+1/N\). Its finitely many coefficients are uniformly
bounded and holomorphic on slightly larger compacts.
For any holomorphic \(A\), the difference
\(\mathcal L_{N,W}A-\sigma_N A\) is a bounded linear
combination of
\[
                       A(a+j/N,y)-A(a,y),\qquad j=1,2.
\tag{25}
\]

Start with \(A_N=O(N)\) from (12) on a larger neighborhood.
Cauchy's estimate makes (25) \(O(1)\) on a smaller
neighborhood. Equation (13), divided by (24), improves
the bound to \(A_N=O(1)\) there. A second Cauchy estimate
then makes (25) \(O(N^{-1})\) on a still smaller neighborhood.
Thus
\[
 A_N=-\frac1{\sigma_N}+O(N^{-1})
      =-\frac1{(W-1)(X^{-1}-1)}+O(N^{-1}).
\]
Nested Cauchy estimates for this holomorphic error prove
the fixed-jet assertion. No estimate for the complete
conditional sum, or for a selected critical contribution,
is used in this argument. \(\square\)

The coefficient in (23) is nonzero. Equations (21), (23)
therefore determine a particular packet with both full
periodic factors, including their exact zeros, rather than
a division-defined packet restricted away from those zeros.

## 4. Calibration with the original observed endpoint

Restore the original Fourier output by setting
\(Y=e^{2\pi iy}=W^{-1}\) and
\[
 \mathcal G^{\rm part}_{-2,N}
       =\frac{\kappa^{-2}e^{\pi i(N-1)y}}N F_N^{\rm part}.
\tag{26}
\]
The exact observed first channel after two negative crossings is
\[
 \mathcal P_{-2,N}
  =\frac{\kappa^{-2}e^{-\pi i(N-1)y}
       X^{-(N-1)}(1-X^N)(1-Y^N)}
          {N^3(1-X)(1-Y)},
\tag{27}
\]
from [the negative-two observation payment](research_mixed_fourier_negative_two_projection_payment.md).
Let
\[
                       A_0(a,y)=-\frac{XY}{(1-X)(1-Y)} .
\]
The finite identities
\[
 X^{-(N-1)}(1-X^N)=X(X^{-N}-1),\qquad
 e^{-\pi i(N-1)y}(1-Y^N)
               =-Y e^{\pi i(N-1)y}(1-Y^{-N})
\]
give, exactly,
\[
 \boxed{\quad
 \mathcal G^{\rm part}_{-2,N}
             =\mathcal P_{-2,N}\,\frac{A_N}{A_0},\qquad
 \frac{A_N}{A_0}=1+O(N^{-1}).
 \quad}
\tag{28}
\]
Only the nonzero analytic coefficient \(A_0\) is divided
out. The finite factors in (27) have not been divided,
so (28) is valid at every physical incoming node lying in
the admitted parameter domain, and for all parameter jets there.

In particular the existing allocated endpoint gap applies
to this entire particular contribution. On the original
incoming plateau, for actual references and \(y=x_0\),
the raw margin \(387/70000\) and (28) imply
\[
 |d_N(X)|^{\eta/2}|\mathcal G^{\rm part}_{-2,N}|
                 \le e^{N\{B_\eta(x)-1/200\}}
\tag{29}
\]
for sufficiently large \(N\), with both parities and the
original incoming halfweight retained. The local ratio to
the original complete cap has the corresponding exponential
fixed-jet bound by the same strict raw margin and nested
Cauchy estimates.

The complete twice-crossed function is now exactly the sum
of (26) and
\(\kappa^{-2}e^{\pi i(N-1)y}F_N^{\rm hom}/N\).
The latter solves the original homogeneous second-order
incoming equation and retains the actual finite contour
normalization. It has not been identified with one of its
critical branches. A bound and noncancellation theorem for
that homogeneous term remain necessary for a complete
twice-crossed asymptotic. This exact decomposition does
not replace that obligation by a formal characteristic
equation.

## 5. The remaining homogeneous contour is explicit

The endpoint-current theorem writes the full source exactly
as \(F_N=I_N+J_N\), where
\[
 I_N=N\int_{\alpha_N}^{\alpha_N+1}T_N(u)\,du,\qquad
 J_N=iN\int_{\mathbb R}w_{N,0}(v)
       [T_N(\alpha_N+1+iv)-T_N(\alpha_N+iv)]\,dv.
\]
Set
\[
 a_0=X^{-N}-1,\qquad b_0=W^N-1,\qquad
 t=e^{-2\pi iN(\alpha_N+iv)}=-e^{2\pi Nv}.
\]
Combining this exact current with (21) gives
\[
 \boxed{\quad
 F_N^{\rm hom}
   =I_N+iN\int_{-\infty}^0 K_-(t)T_N(\alpha_N+iv)\,dv
        +iN\int_0^\infty K_+(t)T_N(\alpha_N+iv)\,dv ,
 \quad}
\tag{30}
\]
where
\[
 K_+(t)=\frac{a_0-b_0t-a_0b_0t/2}{(1-t)^2},\qquad
 K_-(t)=\frac{t(a_0-b_0t+a_0b_0/2)}{(1-t)^2}.
\tag{31}
\]
All displayed integrals converge with the previously proved
tail estimates.

For the algebra, the exact period multiplier gives
\[
 \frac{T_N(s+1)-T_N(s)}{T_N(s)}
   =\frac{a_0-(a_0+b_0+a_0b_0)t+b_0t^2}{(1-t)^2}.
\]
Above height zero, multiply this by \(1/(1-t)\);
below height zero, multiply it by \(t/(1-t)\).
Subtracting the particular current adds
\(a_0b_0t(1+t)/(2(1-t)^3)\) in either case.
One factor \(1-t\) cancels and gives precisely (31).
This is algebra on the original contour, not a modulus estimate.
Neither the zero mode nor these two remaining signed currents
has been discarded. Equation (30) fixes the exact homogeneous
remainder whose critical contributions still require analysis.
