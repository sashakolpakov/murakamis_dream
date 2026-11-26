# An averaged Hermite co-source row for the regular filling factor

Private written proof, 18 November 2026.

The original filling functional annihilates an explicit one-cell
average after its actual sine and Gaussian factors are retained.
The resulting local symbol is the divided exponential, with its
zero-charge zero removed. This is an equation for the closing
functional. It is not an equation annihilating an arbitrary boundary
source, and it does not by itself identify that source's phase with
the full peripheral word.

The complete proof directs are **N**, the finite Newton calculus
`../papers/newton-calculus/finite.tex`, and **R**,
`research_regular_primitive_filling_factor.md`. The exact averaging,
endpoint, and local symbol arguments are proved below.

## 1. The literal row and its normalization

Fix an integer \(N\ge2\), put \(d=N-1\), and use the actual lifts
\[
 q=e^{\pi i/N},\qquad h=\frac{2\pi i}{N},\qquad
 a=\frac{2\pi}{N}=-ih,\qquad \eta=(-1)^d.
 \tag{1}
\]
Here \(a\) denotes the grid spacing, not a primitive slope coefficient.
The full pair algebra and its actual cylindrical trace are
\[
 \mathcal H_N=\mathbb C[z]/(\chi_N),\qquad
 \chi_N(z)=2T_N(z/2)+2,
 \qquad
 \phi(F)=\eta N^2[z^d](F\bmod\chi_N).
 \tag{2}
\]
The factor in (2) includes the original single reduced cut. It is
not an additional normalization to be inserted at every auxiliary
circle of an unrelated presentation.

Let \(R\) be the physical crossing in N. For any signed integer \(n\),
define the entire centered Gaussian and its sine weight by
\[
 f_{N,n}(t)=q^{nd^2/4}\exp\!\left(-\frac{nt^2}{2h}\right),
 \qquad w_{N,n}(t)=\sin t\,f_{N,n}(t),\qquad z(t)=-2\cos t.
 \tag{3}
\]
The fractional power of \(q\) means its displayed exponential lift.
At
\[
 t_j=-\pi+(j+\tfrac12)a,\qquad 0\le j<N,
 \tag{4}
\]
the Gaussian has exactly the values and first \(z\)-derivatives of
\(R^n\), including negative powers. Indeed \(z(t_j)=c_j\) in N and
\[
 f_{N,n}(t_j)
 =q^{nd^2/2}(-1)^{nj}q^{nj(j+1)}.
 \tag{5}
\]
Differentiating (3) in \(t\), then dividing by \(z'(t)=2\sin t\),
gives N's crossing normal multiplied by \(n\). At the odd-level
simple node \(t=0,z=-2\), (3) is even and holomorphic in \(z+2\);
only its value is required.

For an arbitrary polynomial \(H(z)\), with no degree restriction,
write \(H_t(t)=H(z(t))\). Define the normalized filling row
\[
 \mathcal L_N^n(H)=\frac{\phi(R^nH)}{\eta N^2}.
\]
The full Hermite trace in N gives exactly
\[
 \boxed{\quad
 \mathcal L_N^n(H)
   =\frac1{N^2}\sum_{j=0}^{N-1}
        \left.\frac{d}{dt}
             [w_{N,n}(t)H_t(t)]\right|_{t=t_j}.
 \quad}
 \tag{6}
\]
For a double node, its two occurrences \(t,-t\) contribute
\((4-c^2)(R^nH)'(c)-c(R^nH)(c)\), divided by \(N^2\).
When \(N\) is odd, \(t=0\) occurs once and differentiating the sine
gives \((R^nH)(-2)/N^2\). Thus (6) has neither lost a normal nor
doubled the simple node.

More generally (6) defines the same row on compatible holomorphic
germs at the spectral nodes: take their unique degree-\(<N\) Hermite
representative. At a double root both the value and first derivative
are retained. This extension does not change the original functional.

Every finite short Conway expression made from the original signed
crossings, multiplication, turns, and prescribed contractions yields
such a polynomial in each uncontracted spectral variable. This follows
by induction from N's polynomial commutant and linear turn. Products
at a free variable may be left unreduced. All other source variables,
polynomial coupons, and previously specified scalar factors may remain
as spectators in (6).

## 2. The exact averaged row and its boundary current

For an entire function \(g(t)\), let
\[
 (\mathcal A_Ng)(t)
 =\int_{-1/2}^{1/2}g(t+a\rho)\,d\rho
 =\frac1a\int_{t-a/2}^{t+a/2}g(v)\,dv.
 \tag{7}
\]
For the original polynomial \(H\), define
\[
 (\mathcal K_{N,n}H)_t(t)
 =\frac{\mathcal A_N(w_{N,n}H_t)(t)}{w_{N,n}(t)}.
 \tag{8}
\]
The right side is initially defined where \(\sin t\ne0\).
Its numerator is entire and odd: \(w_{N,n}H_t\) is odd, and the
averaging interval is symmetric. Consequently the apparent pole
at \(t=0\) is removable, and (8) is even and holomorphic there.
Since \(z(t)+2=t^2+O(t^4)\), it defines a holomorphic germ in \(z\)
at the odd simple node. Every other midpoint has nonzero sine.
Evenness identifies the two germs over every double spectral node,
including their first \(z\)-derivatives. Thus the left side of
\[
                    \boxed{\mathcal L_N^n(\mathcal K_{N,n}H)=0}
 \tag{9}
\]
is well-defined by the full Hermite convention of Section 1.

Here is the complete endpoint proof of (9). Differentiating (7) gives
\[
 (\mathcal A_Ng)'(t)=\frac{g(t+a/2)-g(t-a/2)}a.
 \tag{10}
\]
The adjacent endpoints in (4) agree. Therefore
\[
 \begin{aligned}
 \mathcal L_N^n(\mathcal K_{N,n}H)
 &=\frac1{N^2}\sum_j(\mathcal A_N(w_{N,n}H_t))'(t_j)\\
 &=\frac{w_{N,n}(\pi)H_t(\pi)
              -w_{N,n}(-\pi)H_t(-\pi)}{N^2a}=0.
 \end{aligned}
 \tag{11}
\]
Both original endpoints have been retained; the last equality uses
their sine zeros. No periodic continuation of the Gaussian, and no
off-grid identification of its branches, has been used.

For a consecutive block \(j=r,\ldots,s\), the exact current instead is
\[
 \frac1{N^2}\sum_{j=r}^{s}
      (\mathcal A_Ng)'(t_j)
 =\frac{g(t_s+a/2)-g(t_r-a/2)}{N^2a}.
 \tag{12}
\]
This is the forcing to retain when a proper portion of the original
row is isolated. In physical trace normalization multiply (11)--(12)
by \(\eta N^2\). Arbitrary other source contractions commute with
these scalar-variable operations by linearity, so (9) holds for the
whole unreduced short-component boundary polynomial, with all its
spectators and original scalar factors.

The output of (8) need not be a polynomial globally. Nor is (8)
asserted to descend to an operator on arbitrary representatives of
\(\mathcal H_N\): it uses \(H\) between grid points. Equality of
Hermite jets alone does not identify those intermediate values.
One may take the Hermite representative of the OUTPUT to evaluate
(9), but must not silently replace its INPUT before averaging.
The theorem is a co-source equation
\(\mathcal L_N^n\circ\mathcal K_{N,n}=0\) on the recorded functions.
It does not say \(\mathcal K_{N,n}H=0\).

## 3. Local symbol, including the complete point

There is an elementary analytic symbol calculation for this exact row.
In this section \(h\) may vary near zero solely to describe its local
analytic family; the finite identity (9) is asserted at the physical
values (1).

Let \(S(t)\) and \(A(t)\) be even holomorphic functions on a fixed disk
about zero, with \(A\) nonzero there. Use the test function
\[
 H_h(t)=e^{S(t)/h}A(t),\qquad
 \Phi(t)=S(t)-\frac n2t^2.
 \tag{13}
\]
This describes an analytic phase on the original ramified Casimir
chart. It is not an assertion that every actual short-component
polynomial has one such phase.

After the scalar in (3) cancels on the two sides of (8), the exact
formula is
\[
 e^{-S(t)/h}(\mathcal K_{h,n}H_h)(t)
 =\frac1{\sin t}
  \int_{-1/2}^{1/2}\sin(t-ih\rho)A(t-ih\rho)
   \exp\!\left(\frac{\Phi(t-ih\rho)-\Phi(t)}h\right)d\rho.
 \tag{14}
\]
The exponent quotient extends holomorphically to \(h=0\), by the
integral identity
\[
 \frac{\Phi(t-ih\rho)-\Phi(t)}h
    =-i\rho\int_0^1\Phi'(t-i\theta h\rho)\,d\theta.
 \tag{15}
\]
On a smaller \(t\)-disk all arguments remain in the original disk
for small \(h\). The numerator in (14) is jointly holomorphic in
\((t,h)\), and is odd in \(t\) by replacing \(\rho\) with \(-\rho\).
It is therefore divisible by \(t\), jointly; \(\sin t/t\) is a unit.
This proves joint removability at \(t=0\), without a \(1/t\) error
bound. Substituting \(h=0\) gives, uniformly on smaller closed disks,
\[
 e^{-S/h}\mathcal K_{h,n}H_h
       = A(t)\,J(s(t))+O(h),\qquad
 s(t)=i\{S'(t)-nt\},
 \tag{16}
\]
where the remainder is holomorphic and uniformly bounded after
division by \(h\), and
\[
 \begin{aligned}
 J(s)&=\int_{-1/2}^{1/2}e^{-\rho s}\,d\rho
       =\frac{\sinh(s/2)}{s/2}
       =e^{-s/2}\psi(s),\\
 \psi(s)&=\frac{e^s-1}s,\qquad J(0)=\psi(0)=1.
 \end{aligned}
 \tag{17}
\]
The nonzero zeros of \(J\) are exactly \(2\pi i\mathbb Z\setminus\{0\}\),
and each is simple. At \(t=0\) an even phase has \(s(0)=0\), so
the symbol is one there. The conclusion holds uniformly with
holomorphic spectator parameters on compact sets satisfying the
same disk and unit conditions. Away from the sine zeros the same
symbol calculation does not require evenness.

The averaged row therefore retains the divided-exponential factor,
rather than only its product with \(s\). This follows directly from
the finite Hermite derivative sum. It is not deduced by dividing a
quantum eigenvalue equation by a vanishing operator.

## 4. The regular primitive word and the limit of the conclusion

Retain a regular marked peripheral chart as in R, with centered logs
\(U,V=U\tau\), meridian translation \(B\ne0\), and
\(\Im\tau>0\). For a primitive word with integer coefficients
\((\mathfrak a,\mathfrak b)\), R proves
\[
 t_{\mathfrak a,\mathfrak b}
   =(\mathfrak a+\mathfrak b\tau)
         \frac{\psi(\mathfrak aU+\mathfrak bV)}{\psi(U)},
 \qquad
 \mu^{\mathfrak a}\lambda^{\mathfrak b}=1
       \Longleftrightarrow t_{\mathfrak a,\mathfrak b}=0.
 \tag{18}
\]
On its complete chart \(\psi(U)\) and
\(\mathfrak a+\mathfrak b\tau\) are units. If the actual retained
source-word adapter identifies the momentum in (16) with
\[
             s(t)=\mathfrak aU(t)+\mathfrak bV(t),
 \tag{19}
\]
then the computed symbol is exactly
\[
 J(s(t))=
 \frac{e^{-s(t)/2}\psi(U(t))}
              {\mathfrak a+\mathfrak b\tau(t)}
                     t_{\mathfrak a,\mathfrak b}(t).
 \tag{20}
\]
The prefactor is a nonvanishing holomorphic function on that chart.
Thus this literal co-source row has the regular primitive factor as
its symbol up to the displayed unit, including at the complete point.
For the physical integer-twist convention, (19) is the adapter for
that actual primitive slope; an arbitrary rational surgery kernel
has not been supplied by the present argument.

Equation (20) does not prove (19) for an arbitrary continued branch of
an arbitrary short component. It does not turn a retained Casimir
normal into a transverse solution of the classical filling equations.
Nor does (9) imply that every contribution to a closed source lies
on the regular characteristic set: localization and inverse transport
must keep the currents (12), any other boundary pieces, and the same
input representative. In particular no full matrix relation for all
source critical points, selected geometric coefficient, or scalar
lower bound is inferred here.

## Complete proof-source pins

* N: `../papers/newton-calculus/finite.tex`, SHA256
  `2db2d7e15df0210c32bace4c761bdabadbb5d67140473a61425dac4d1e382f8e`.
* R: `research_regular_primitive_filling_factor.md`, SHA256
  `ac4a336eac370bb45aec59b7a95de9e2884448d861a10b3f021f5d45d2bf76c4`.
