# Exact homogeneous periods of the twice-crossed conditional source

Research deduction, 7 November 2026. The complete homogeneous
remainder has a cut-independent contour expression: its horizontal
period can be moved to the actual critical height while all joining
terms remain in the same expression. A second explicit contour
integral is a nontrivial homogeneous solution. It is exponentially
small on every compact subset of the original parameter domain,
although it is not identically zero.

The exact two-variable Casoratian of these periods is computed
below. Its remaining periodic factor is fixed by the growth of
the original contour integrals, so the pair is nondegenerate on
the full fixed-level state domain. This does not yet identify the
complete remainder with a single contributing critical cycle.
No numerical evaluation is used.

## 1. The complete remainder is independent of its horizontal cut

Use the original \(T_N(s;a,y)\), operator \(\mathcal L_{N,W}\),
and exact decomposition
\[
 C_{0,N}(X,W)=F_N^{\rm part}(a,y)+F_N^{\rm hom}(a,y)
\]
from
[the particular-current theorem](research_mixed_three_fourier_conditional_particular_current.md).
Here \(X=e^{-2\pi ia}\), \(W=e^{-2\pi iy}\), and
\[
 0<\Re a,\Re y<1/2,\qquad \Im y>0,\qquad
 \alpha_N=-1/(2N),\quad \beta_N=\alpha_N+1.
\tag{1}
\]
Set
\[
 a_0=X^{-N}-1,\qquad b_0=W^N-1,\qquad t=e^{-2\pi iNs},
\]
\[
 K_+(t)=\frac{a_0-b_0t-a_0b_0t/2}{(1-t)^2},\qquad
 K_-(t)=\frac{t(a_0-b_0t+a_0b_0/2)}{(1-t)^2}.
\tag{2}
\]
The original period identity gives, on the left vertical line,
\[
 \boxed{\quad
 [K_+(t)-K_-(t)]T_N(s)
                         =T_N(s+1)-T_N(s).
 \quad}
\tag{3}
\]
Indeed its difference multiplier is
\[
 \frac{a_0-(a_0+b_0+a_0b_0)t+b_0t^2}{(1-t)^2},
\]
which is the difference of the two expressions in (2).
On that line \(t=-e^{2\pi N\Im s}\), so no displayed
denominator vanishes. Formula (3) is an undivided identity
and retains every numerator zero.

**Proposition 1.** For every finite real \(H\), the complete
homogeneous remainder is exactly
\[
 \boxed{\begin{split}
 F_N^{\rm hom}
   ={}&N\int_{\alpha_N+iH}^{\beta_N+iH}T_N(s)\,ds\\
     &+N\int_{\alpha_N-i\infty}^{\alpha_N+iH}
                             K_-(e^{-2\pi iNs})T_N(s)\,ds\\
     &+N\int_{\alpha_N+iH}^{\alpha_N+i\infty}
                             K_+(e^{-2\pi iNs})T_N(s)\,ds .
 \end{split}}
\tag{4}
\]
Both vertical integrals are oriented upward. Their tails
converge absolutely with the original factorial bounds.

*Proof.* At \(H=0\), (4) is exactly equations (30)--(31) of
the particular-current theorem, with \(ds=i\,dv\).
The derivative of its horizontal term with respect to \(H\)
is
\[
 iN[T_N(\beta_N+iH)-T_N(\alpha_N+iH)].
\]
The derivative of the sum of its vertical terms is
\[
 iN[K_-(t)-K_+(t)]T_N(\alpha_N+iH).
\]
They cancel by (3). All finite intervening rectangles are
in the original holomorphic factorial chart. The fixed
infinite ends are controlled by the existing uniform tail
estimates, and are not moved in this differentiation.
Thus (4) holds at every finite height. \(\square\)

This is a closed contour expression under the exact one-period
row relation. It is not a periodic replacement of individual
shifted factorials. In particular on the actual type-three
input rectangle one may set \(H=\Im s_*(a)>0\), using the
critical branch of
[the complete left zero-mode theorem](research_mixed_three_fourier_conditional_left_zero_mode.md).
That puts the full horizontal period through its proved left
critical point without discarding either joining current.
The right part of this expression still has to be analyzed
coherently before a contributing-cycle conclusion follows.

## 2. A second exact homogeneous contour integral

Define the second-order periodic kernel and its upward integral
\[
 k_{2,N}(s)=\frac{e^{-2\pi iNs}}{(1-e^{-2\pi iNs})^2},\qquad
 \mathcal I_{2,N}(a,y)=
   \int_{\alpha_N-i\infty}^{\alpha_N+i\infty}
                         k_{2,N}(s)T_N(s;a,y)\,ds .
\tag{5}
\]
The function is defined by this integral, not by an asymptotic
formula.

**Proposition 2.** Uniformly on every compact subset of (1),
\[
             |\mathcal I_{2,N}|\le CN^{-2},\qquad
                    \mathcal L_{N,W}\mathcal I_{2,N}=0
\tag{6}
\]
for all sufficiently large \(N\). The integral is holomorphic
in both parameters.

*Proof.* On the half-grid line put \(T=e^{2\pi Nv}>0\).
Then
\[
 |k_{2,N}(\alpha_N+iv)|=\frac{T}{(1+T)^2}
                                  \le |w_{N,0}(v)|\quad(v\ne0).
\]
The exact midpoint estimate and the complete left-side tail
bound in
[the endpoint-current theorem](research_mixed_three_fourier_conditional_endpoint_current.md)
therefore give \(CN^{-2}\) for the integral of the absolute
value. The same compact-uniform bounds imply holomorphy.

Use the exact telescoper
\[
 \mathcal L_{N,W}T_N(s)=B_N(s)-B_N(s+1/N),\qquad
 B_N(s)=(e^{2\pi is}-1)^2T_N(s).
\]
Shifting the second vertical line by \(1/N\) leaves just
the pole at \(s=0\) between the two lines. In this case it
has been canceled completely:
\[
 k_{2,N}(s)=\frac1{(2\pi iNs)^2}+O(s^{-1}),\qquad
 B_N(s)=(2\pi is)^2+O(s^3).
\]
Thus \(k_{2,N}B_N\) is holomorphic at zero and has no residue.
The upper horizontal connector decays with exponent
\(-2\pi N(1-\Re y)H\); the lower one has exponent
\(-2\pi\{N(1-\Re a)-2\}H\).
These are strictly negative for sufficiently large \(N\),
uniformly on the fixed compact set. There are no other
factorial or kernel poles in the small intervening strip.
Cauchy's theorem now gives the second identity in (6).
\(\square\)

## 3. The period is nontrivial, despite exponential flatness

For each fixed \(N\), the integral (5) extends holomorphically
to the connected larger domain
\[
 -\frac1{2N}<\Re a<1,\qquad
 -\frac1{2N}<\Re y<1 ,
\tag{7}
\]
with arbitrary imaginary parts. This statement asserts no
uniform large-\(N\) bound near the new edges.
On the left vertical contour both numerator arguments have
real part greater than \(-1/N\); the parameter reciprocals
and \(E_N(s)\) are in their original holomorphic domains.
The exact upper and lower factorial formulas give tail
decay \(2\pi N(1-\Re y)\) and \(2\pi N(1-\Re a)\).
These remain strict on each fixed-level compact subset of
(7), so the same integral defines the continuation.

At \(a=y=0\), its original row is identically one. Since
\[
 k_{2,N}(s)=
   -\frac1{2\pi iN}\frac{d}{ds}
                   \left(\frac1{1-e^{-2\pi iNs}}\right),
\]
and the expression in parentheses decreases from \(1\) to
\(0\) along the upward half-grid line, the exact anchor is
\[
                       \boxed{\mathcal I_{2,N}(0,0)=\frac1{2\pi iN}.}
\tag{8}
\]
Consequently \(\mathcal I_{2,N}\) is not identically zero
on (7), or on the connected open subdomain (1). This
argument does not assert nonvanishing at every actual
incoming parameter.

There is nevertheless a stronger smallness statement on
every fixed compact subset of (1).

**Proposition 3.** For such a compact set \(K\), there are
constants \(C,\gamma>0\) such that
\[
                         \sup_K|\mathcal I_{2,N}|
                                  \le C e^{-\gamma N}.
\tag{9}
\]
All fixed parameter derivatives have the same type of bound
on smaller compact subsets.

*Proof.* The constant-shift coefficient of the exact operator
is
\[
 \sigma_N=\mathcal L_{N,W}1
                 =(r^{-1}-W)(1-r^{-1}X^{-1}).
\]
On a slightly larger fixed parameter neighborhood it has
a positive uniform modulus for all large \(N\).
All coefficients in the shift expansion of \(\mathcal L\)
are uniformly bounded there. Its homogeneous equation
therefore bounds a holomorphic solution \(f\) on a smaller
set by a constant times its differences
\(f(a+j/N,y)-f(a,y)\), \(j=1,2\).

Choose a fixed \(a\)-neighborhood of width \(R>0\) between
\(K\) and the boundary of this larger parameter domain.
Cauchy's estimate, on nested sets whose \(a\)-widths differ
by \(\delta\ge4/N\), gives
\[
             \|f\|_{\rm inner}
                  \le \frac{C_0}{N\delta}\|f\|_{\rm outer}.
\tag{10}
\]
The shifts by \(j/N\) stay in the outer set; the numerical
factor in this Cauchy bound is absorbed in \(C_0\).
All constants are independent of the particular nested
pair inside the chosen fixed neighborhood.

Take a fixed \(L>\max(4,2C_0)\), put \(\delta=L/N\),
and iterate (10) through
\(m=\lfloor RN/L\rfloor\) nested neighborhoods. Each step
costs at most \(1/2\). The outer bound (6) yields
\[
 \sup_K|\mathcal I_{2,N}|
       \le CN^{-2}2^{-m}
       \le 2CN^{-2}
               e^{-(R\log2)N/L}.
\]
Finite covers handle a general compact \(K\); a final fixed
buffer and Cauchy's estimate give the parameter derivative
assertion. This uses the exact homogeneous equation and
the uniform polynomial contour bound, not a claim that
superpolynomial decay implies zero. \(\square\)

The exact anchor (8) and the exponential bound (9) are
consistent: the anchor is outside every fixed compact
subset of (1), where the constant-shift symbol is separated
from zero.

## 4. Exact Casoratian transport and every physical two-point state

Write \(H_N=F_N^{\rm hom}\), \(Z_N=\mathcal I_{2,N}\), and
\(\delta=1/N\) in this section. The symbol \(Z_N\) here
denotes only the second homogeneous period, not the earlier
Fourier cap. Both functions extend to the fixed-level strip
product (7). For \(H_N\), this is the same-current extension
proved in
[full-node composition](research_mixed_three_homogeneous_period_full_node_composition.md).
It gives
\[
 H_N(b/N,c/N)=C_{0,N}(r^b,r^c)
                       \quad(0\le b,c<N).
\tag{11}
\]
Define the incoming Casoratian by
\[
 \mathcal W_N(a,y)
       =H_N(a,y)Z_N(a+\delta,y)
                            -H_N(a+\delta,y)Z_N(a,y).
\tag{12}
\]
Its fixed-level domain has
\(-1/(2N)<\Re a<1-\delta\), \(y\) in (7).

The second-order equation, expanded in the incoming shift,
has highest and lowest coefficients
\[
 A_2=-\frac{(1-rX)(1-r^2X)^2}{r^2X},\qquad
 A_0=(1-rX)^2.
\]
Consequently, on the shifted regular domain,
\[
 \mathcal W_N(a+\delta,y)
   =-\frac{r^2X(1-rX)}{(1-r^2X)^2}\mathcal W_N(a,y).
\tag{13}
\]
This is the exact discrete Wronskian relation \(A_0/A_2\);
it is independent of \(W=e^{-2\pi iy}\).

There is also an exact outgoing relation. Define
\[
 \mathsf E_y=\frac{1-(1-rW)\mathsf T_y}{rW},\qquad
                    (\mathsf T_yf)(a,y)=f(a,y+\delta).
\]
The literal factorial row satisfies
\(\mathsf E_yT_N(s)=e^{-2\pi is}T_N(s)\).
Thus
\[
                      \mathsf D_X\mathsf E_y f=f
\tag{14}
\]
for \(f=H_N,Z_N\). For the integral terms this follows
under the convergent contour; for the finite sum it follows
termwise. The particular forcing factors are invariant
under both shifts, so subtraction preserves (14).
No physical-node specialization is made in this argument.

Here is the resulting state relation explicitly. Put
\(c=1-rX,\ d=1-rW\) and
\(\mathbf v_f=(f(a,y),f(a+\delta,y))^T\). Equations
(14) and the incoming second-order equations at \(W\)
and \(rW\) give
\[
 d\begin{pmatrix}
       rX&c\\ c&rX+W/X-2
    \end{pmatrix}\mathbf v_f(y+\delta)
   =
    \begin{pmatrix}
       r(X-W)&c\\ c&rX+rW-2
    \end{pmatrix}\mathbf v_f(y).
\tag{15}
\]
One first derives (15) with \(\Re a<1-2\delta\).
After elimination it contains only the states at \(a,a+\delta\),
so holomorphy extends this undivided matrix identity to
\(\Re a<1-\delta,\ \Re y<1-\delta\) in the fixed-level
strip product. The determinants of its two displayed
matrices are \(-d\) and \(-d^2\), respectively. Wherever
\(d\ne0\), it follows that
\[
                 \mathcal W_N(a,y+\delta)
                       =\frac{\mathcal W_N(a,y)}{1-rW}.
\tag{16}
\]

The initial Casoratian is exact and nonzero. Equation (11)
and the elementary finite geometric sum give
\[
 H_N(0,0)=N,\qquad
 H_N(\delta,0)=-\frac{Nr}{1-r}.
\]
At the same points (8) gives \(Z_N(0,0)=1/(2\pi iN)\).
For the other value, the row is
\[
           T_N(s;\delta,0)=\frac{e^{2\pi is}-r}{1-r}.
\]
On the upward half-grid line the substitution
\(T=e^{2\pi Nv}\) evaluates its elementary beta integral:
\[
 Z_N(\delta,0)=
  \frac{e^{-\pi i/N}(\pi/N)/\sin(\pi/N)-r}
                         {(1-r)2\pi iN}.
\tag{17}
\]
Indeed the additional factor \(e^{2\pi is}\) changes
\(\int_0^\infty(1+T)^{-2}\,dT=1\) to
\[
 \int_0^\infty\frac{T^{-1/N}}{(1+T)^2}\,dT
     =\Gamma(1-1/N)\Gamma(1+1/N)
     =\frac{\pi/N}{\sin(\pi/N)}.
\]
This is an analytic identity, not a numerical evaluation.
Substitution into (12), with
\(1-r=2i e^{-\pi i/N}\sin(\pi/N)\), gives
\[
                    \boxed{\mathcal W_N(0,0)
                              =-\frac1{4N\sin^2(\pi/N)}\ne0.}
\tag{18}
\]

**Proposition 4.** For \(N\ge3\), every full physical
two-point incoming state satisfies
\[
 \boxed{\quad
 \mathcal W_N(b/N,c/N)=
    \frac rN\,
    \frac{e^{\pi i\{b-(b^2+3b)/N\}}}
          {(1-r^{b+1})^2P_bP_c}\ne0,
 \quad
 0\le b\le N-2,\quad0\le c\le N-1.
 \quad}
\tag{19}
\]

*Proof.* Propagate (18) using (13) through
\(b=0,\ldots,N-3\); these are within the admitted
incoming shifted-equation domain. Then propagate (16)
through \(c=0,\ldots,N-2\). The extended state relation
(15) includes \(b=N-2\), although the uneliminated
second-order equation cannot be imposed there at \(a+2\delta=1\).
None of the propagation denominators vanish in these
stated ranges. Multiplying the ratios, or verifying
the right-hand side in both recurrences and at (18),
gives (19). All its factorial indices are below \(N\),
and \(1-r^{b+1}\ne0\). \(\square\)

Off grid the same calculation isolates the remaining
periodic normalization. Namely
\[
 \mathcal W_N(a,y)
   =\frac rN
       \frac{e^{\pi i\{N(a-a^2)-3a\}}E_N(a)E_N(y)}
            {(1-rX)^2}\,\mathcal P_N(a,y),
\tag{20}
\]
where \(\mathcal P_N\) is holomorphic on the state domain,
\[
 \mathcal P_N(a+\delta,y)=\mathcal P_N(a,y),\qquad
 \mathcal P_N(a,y+\delta)=\mathcal P_N(a,y)
\tag{21}
\]
on their overlaps, and \(\mathcal P_N(0,0)=1\).
The factor outside \(\mathcal P_N\) is nonzero there
and has exactly the ratios (13), (16).
The recurrences by themselves do not fix this periodic
factor. The next section uses the growth of the original
integrals, rather than declaring the factor constant from
the physical anchor.

## 5. The original contour growth fixes the periodic factor

**Theorem 5.** For every \(N\ge5\), on the full fixed-level
state domain
\[
 -\frac1{2N}<\Re a<1-\frac1N,\qquad
 -\frac1{2N}<\Re y<1,
\]
the exact Casoratian is
\[
 \boxed{\quad
 \mathcal W_N(a,y)=
   \frac rN\,
    \frac{e^{\pi i\{N(a-a^2)-3a\}}E_N(a)E_N(y)}
         {(1-rX)^2}\ne0 .
 \quad}
\tag{22}
\]
In particular the two original periods are independent
at every admitted actual complex reference for all
sufficiently large levels.

*Proof.* All growth estimates in this proof are at fixed
\(N\). Their constants may depend on \(N\); no large-level
estimate at a moving endpoint is assumed.
The exact upper and lower factorial formulas, and compactness
between their ends, give a two-sided comparison
\[
 |\Pi_N(z)|\asymp
   \exp\{\pi[N(2\Re z-1)+1](\Im z)_+\}
\tag{23}
\]
uniformly when \(\Re z\) is in any compact subinterval of
the original zero-free strip \((-1/N,1)\). This statement
uses the original Gamma normalization and does not cross
a positive factorial zero.

First take fundamental real strips
\[
 0\le x=\Re a\le2/N,\qquad
 0\le \xi=\Re y\le1/N,
\]
and write \(h=\Im a,\ \upsilon=\Im y\). Let
\[
                  A=N(2x-1),\qquad B=N(2\xi-1).
\]
For \(N\ge5\), both \(A\) and \(B\) are strictly negative.
Every numerator argument on the half-grid line has its
real part in \([-1/(2N),3/(2N)]\), and all parameter
arguments are in the original zero-free strip.
Combining (23) with the exact midpoint reciprocal gives
the following upper exponent, divided by \(\pi\), for
the absolute integrands defining \(Z_N=\mathcal I_{2,N}\)
and \(A_N\):
\[
 \begin{split}
 \mathcal E(v)={}&
 A(v+h)_+-(A+1)h_+
 +B(v+\upsilon)_+-(B+1)\upsilon_+\\
 &-2Nxv+h+2N\min(v,0).
 \end{split}
\tag{24}
\]
For \(A_N\), use \(|k_{3,N}|\le|k_{2,N}|\) on this line.
All constants and fixed powers of \(N\) are harmless in
this fixed-level growth calculation.

Fix \(y\). If \(h\ge0\), the inequality
\(A(v+h)_+\le A(v+h)\) cancels all \(h\)-terms in (24).
The resulting majorant is integrable in \(v\), uniformly
in the displayed real strips: its slopes at the lower
and upper ends are \(N\) and \(2N(\xi-1)\), respectively.
If \(h\le0\), drop \(A(v+h)_+\le0\). The remaining
integrable majorant has the additional constant \(h\).
It follows that
\[
 Z_N(a,y),\,A_N(a,y)=
 \begin{cases}
 O(1),&h\longrightarrow+\infty,\\
 O(e^{\pi h}),&h\longrightarrow-\infty .
 \end{cases}
\tag{25}
\]
The constants are uniform for \(x\in[0,2/N]\), with
\(y\) fixed in its fundamental real strip.

The finite conditional source has incoming band
\([-N+1,0]\). Since
\(H_N=F_N-(1-W^N)(X^{-N}-1)A_N/N^2\), (25) gives
\[
 H_N(a,y)=
 \begin{cases}
 O(1),&h\longrightarrow+\infty,\\
 O(e^{-\pi(2N-1)h}),&h\longrightarrow-\infty .
 \end{cases}
\]
Consequently on \(0\le x\le1/N\), both state entries are
covered and
\[
 \mathcal W_N(a,y)=
 \begin{cases}
 O(1),&h\longrightarrow+\infty,\\
 O(e^{-2\pi(N-1)h}),&h\longrightarrow-\infty .
 \end{cases}
\tag{26}
\]
Divide by the explicit nonzero factor in (20), using
the two-sided estimate (23). Its modulus is comparable
to \(e^{-2\pi h}\) as \(h\to+\infty\), and to
\(e^{\pi(A+3)h}\) as \(h\to-\infty\). Hence
\[
 \mathcal P_N(a,y)=
 \begin{cases}
 O(e^{2\pi h}),&h\longrightarrow+\infty,\\
 O(e^{\pi(N+3)|h|}),&h\longrightarrow-\infty .
 \end{cases}
\tag{27}
\]
These rates are both strictly smaller than \(2\pi N\).

A holomorphic \(1/N\)-periodic function of \(a\) is a
holomorphic function of \(X^N\) on \(\mathbb C^\times\).
The first bound in (27) grows slower than \(|X^N|\)
at infinity. The second grows slower than \(|X^N|^{-1}\)
at zero, because \(N+3<2N\). Laurent coefficient estimates
on circles of arbitrarily large and small radius therefore
kill every nonconstant Laurent mode. Thus
\(\mathcal P_N\) is independent of \(a\). The exact
periodicity on overlaps suffices for this cylinder
argument; no unproved growth continuation is inserted.

It remains to control \(y\). Set \(a=0\) in the Casoratian.
By the physical identities (11),
\(H_N(0,y)\) and \(H_N(\delta,y)\) are the finite
conditional polynomials in \(W\), of degree at most \(N-1\).
They are \(O(e^{2\pi(N-1)\upsilon})\) as
\(\upsilon\to+\infty\) and \(O(1)\) as
\(\upsilon\to-\infty\).
For \(Z_N(0,y)\) and \(Z_N(\delta,y)\), set \(h=0\)
in (24). If \(\upsilon\ge0\), use
\(B(v+\upsilon)_+\le B(v+\upsilon)\), obtaining an
integrable bound with constant \(-\upsilon\).
If \(\upsilon\le0\), drop \(B(v+\upsilon)_+\le0\).
The slopes at both ends remain strict for \(x=0,\delta\).
Thus, uniformly for \(\xi\in[0,1/N]\),
\[
 Z_N(0,y),\,Z_N(\delta,y)=
 \begin{cases}
 O(e^{-\pi\upsilon}),&\upsilon\longrightarrow+\infty,\\
 O(1),&\upsilon\longrightarrow-\infty .
 \end{cases}
\tag{28}
\]
The Casoratian is accordingly
\(O(e^{\pi(2N-3)\upsilon})\) at the positive end and
\(O(1)\) at the negative end. In (20), at \(a=0\),
the only variable factor is \(E_N(y)\), whose positive
growth is
\(e^{\pi(N-2N\xi-1)\upsilon}\) and whose negative
limit is bounded above and below. It follows that
\[
 \mathcal P_N(0,y)=
 \begin{cases}
 O(e^{\pi N\upsilon}),&\upsilon\longrightarrow+\infty,\\
 O(1),&\upsilon\longrightarrow-\infty .
 \end{cases}
\tag{29}
\]
The same Laurent argument, now in \(W^N\), shows that
\(\mathcal P_N\) is independent of \(y\).
Its exact value at \((0,0)\) is one. This proves (22).
The factorial reciprocals have no zeros in the displayed
state strip, and \(1-rX\ne0\) there; the right-hand side
of (22) is therefore nonzero throughout. \(\square\)

On any compact regular parameter chart inside the original
factorial strips, (22) also gives the explicit nonzero
Casoratian packet
\[
 \mathcal W_N(a,y)=N^{-2}
  \frac{e^{-3\pi ia}}
       {(1-X)^2\mathfrak a(a)\mathfrak a(y)}
  e^{N\{\pi i(a-a^2)-g(a)-g(y)\}}
                          (1+O(N^{-1})),
\tag{30}
\]
with every fixed derivative on smaller charts.
Here \(\mathfrak a\) is the original factorial symbol.
This is an asymptotic for the exact period pairing,
not yet a packet for \(H_N\) alone.

The full nondegenerate pairing (22) fixes the normalization
which the physical anchor and difference equations alone
could not fix. A global contributing-cycle theorem for
the complete remainder (4) still requires control of its
full contour or a compatible connection argument. It is
not inferred solely from the nonzero Casoratian.
