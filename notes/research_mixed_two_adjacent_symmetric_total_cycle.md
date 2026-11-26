# A symmetric inner cutoff on the complete total-index cycle

Research deduction, 7 November 2026. At equal Fourier endpoints,
the two endpoint currents of the fixed-total interpolation can be
combined on one cutoff line. Their extra total-period factor
annihilates on the complete outer residue contour. This gives a
different holomorphic representative of the same physical inner
values and an exact formula for any admitted block of total indices.

All complementary total indices remain in the original source.
The remaining current is not declared small. No numerical
evaluation is used.

## 1. The fixed source and the symmetric rectangle

Use [the fixed-total interpolation](research_mixed_two_adjacent_fixed_total_interpolant.md),
equations (4)--(7), at equal external parameters \(x=y\). Put
\[
\begin{gathered}
 r=e^{-2\pi i/N},\quad R=4/5,\quad M_N=\lfloor NR\rfloor,
 \quad \beta=\frac{M_N+1/2}{N},\\
 9/50<\Re x<19/100,\qquad
 2/3<\Re c<\min(4/5,\beta),\qquad N\ge64,\\
 T(a;c,x)=e^{2\pi iNa(c-a)}\Pi_N(c)
       \Pi_N(a+x)\Pi_N(c-a+x)
       E_N(a)^2E_N(c-a)^2E_N(x)^2,\\
 H(c,x)=\sum_{j=0}^{M_N}T(j/N;c,x).
\end{gathered}
\tag{1}
\]
Heights are arbitrary and finite. The strict inequality
\(\Re c<\beta\) holds for all sufficiently large \(N\) on every
fixed compact subset of the original total strip. In particular it
holds near the actual \(c_*=2a_*\) for all sufficiently large levels.

Write \(c=c_r+iv\), set
\[
             L=c_r-\beta<0,\qquad h=v/2.
\tag{2}
\]
The interval \([L,\beta]\) is centered at \(c_r/2\). On its
entire finite-height rectangle the two moving numerator real parts
lie strictly in \((0,1)\): their extrema are
\(c_r-\beta+\Re x\) and \(\beta+\Re x\). For \(N\ge64\),
\[
 c_r-\beta+\Re x>
       2/3-4/5-1/128+9/50>0,\qquad
 \beta+\Re x<4/5+1/128+19/100<1.
\tag{3}
\]
The fixed numerator \(c\) is in its original strip, and both
reciprocal arguments \(a,c-a\) have real part at most
\(\beta<1\). Thus the complete row is holomorphic there, including
its negative-index reciprocal zeros.

The original sampling kernel is
\[
                 k_N(a)=\frac1{1-e^{-2\pi iNa}},
\tag{4}
\]
with residue \(1/(2\pi iN)\). Its added negative physical nodes
inside the wider rectangle contribute zero: \(E_N(j/N)^2=0\)
for every negative integer \(j\) there, while the other factors
remain finite. The nonnegative nodes are exactly \(0,\ldots,M_N\).
Consequently this rectangle gives the same \(H\) in (1).
If its left side passes through a negative physical node, the
product \(k_NT\) is removable there; equivalently one may first
move that cut slightly and take its limit.

The exact symmetry, with its phase included, is
\[
                         T(a;c,x)=T(c-a;c,x).
\tag{5}
\]
It is an identity of the original factorial expressions.

## 2. Combining the entire two endpoint currents

For real \(t\), put
\[
 A=A(t)=e^{2\pi Nt}>0,\qquad
 B=B(c)=e^{-2\pi iNc},\qquad
 w_h(t)=\frac1{1+A(t)}-\boldsymbol1_{\{t<h\}}.
\tag{6}
\]
The right cut is a half-grid cut. The left cut is generally not:
\[
 k_N(\beta+it)=\frac1{1+A(t)},\qquad
 k_N(L+it)=
       \frac1{1+e^{-2\pi iNc_r}e^{2\pi Nt}}.
\tag{7}
\]
No half-grid bound is assigned to that second expression.

**Proposition 1.** At every admitted level and parameter,
\[
\begin{split}
 H(c,x)={}&N\int_{L+ih}^{\beta+ih}T(a;c,x)\,da\\
 &+iN\int_{-\infty}^{\infty}
             W_c(t)\,T(\beta+it;c,x)\,dt ,
\end{split}
\tag{8}
\]
where the product in the second line is interpreted by its
removable continuation and
\[
\begin{split}
 W_c(t)
 &=\frac1{1+A}-\frac{A}{A+B}
                       +\operatorname{sgn}(t-h)\\
 &=2w_h(t)+(B-1)\frac{A}{(1+A)(A+B)} .
\end{split}
\tag{9}
\]
The value at \(t=h\) does not affect the integral. Both tails of
the complete product are absolutely integrable at fixed \(N\),
locally uniformly in the parameters.

*Proof.* Apply the original positive residue contour to the
rectangle in Section 1. As in the fixed-total contour theorem,
remove both horizontal aliases before moving the unweighted
horizontal integral to height \(h\). On a general vertical cut
its remaining weight is \(k_N(a)-\boldsymbol1_{\{t<h\}}\).
The right side is upward and the left side downward.

The exact factorial tail polynomials are those in equations
(11)--(14) of the fixed-total note. On the present wider real
interval their upper and lower alias slopes are respectively
\[
 \pi\{N(1+2c_r-2\Re x-2u)+1\},\qquad
 \pi\{N(1-2\Re x+2u)+1\}.
\tag{10}
\]
The first is minimized at \(u=\beta\), the second at
\(u=L=c_r-\beta\). Both minima equal the same expression and
are greater than \(\pi N/3\), by (1) and
\(2\beta\le8/5+1/N\). These exact fixed-level estimates justify
alias removal and both original side integrals. Their constants
are uniform on compact parameter sets at the fixed level.

Now substitute \(t\mapsto v-t\) in the entire left integral.
Equation (5) gives
\[
                T(L+i(v-t);c,x)=T(\beta+it;c,x),
\]
while (7) becomes \(A/(A+B)\). Since \(v-h=h\), the left
indicator becomes \(\boldsymbol1_{\{t>h\}}\). Subtracting
the left weight from the right weight gives the first line
of (9), with exactly the sign in (8). The second line of
(9) follows from
\[
          1-\frac1{1+A}-\frac{A}{A+B}
                =(B-1)\frac{A}{(1+A)(A+B)}.
\tag{11}
\]
This proves the formula wherever the displayed kernels have
no pole on their lines. Section 3 gives its removable form,
which proves the remaining cases as well. \(\square\)

At a physical total \(c=m/N\), \(B=1\), \(v=h=0\). The
combined current is exactly twice the right current:
\[
 H(m/N,x)
  =N\int_{m/N-\beta}^{\beta}T(a;m/N,x)\,da
       +2iN\int_{\mathbb R}w_0(t)T(\beta+it;m/N,x)\,dt .
\tag{12}
\]
The added real endpoints in the first integral are not
discarded physical rows; their complete contour is retained.

## 3. Removing the apparent pole without division by a zero

On the right line let \(T^{\rm ref}(\beta+it;c,x)\) denote the
same row as in (1), with only \(E_N(c-\beta-it)^2\) replaced
by \(E_N(c-\beta+1-it)^2\). The new reciprocal argument has
real part strictly between zero and one by (1). Every other
argument retains its domain. Thus \(T^{\rm ref}\) is
holomorphic in \(c,x\), for every real \(t\).

The exact reciprocal period identity gives
\[
 T(\beta+it;c,x)
       =\left(1+\frac BA\right)^2
                           T^{\rm ref}(\beta+it;c,x).
\tag{13}
\]
In particular a possible zero \(A+B=0\) has not been divided
out. The extra product in the second line of (9) is exactly
\[
 \frac{A}{(1+A)(A+B)}T(\beta+it;c,x)
       =\frac{A+B}{A(1+A)}
                           T^{\rm ref}(\beta+it;c,x).
\tag{14}
\]
The right side is holomorphic in all the free parameters.
It also shows that the apparent kernel pole has a zero,
rather than a residual singularity, in the complete product.

Define the full, untruncated integral
\[
 I_N(c,x)=\int_{-\infty}^{\infty}
          \frac{A(t)+B(c)}{A(t)(1+A(t))}
                   T^{\rm ref}(\beta+it;c,x)\,dt .
\tag{15}
\]
This is holomorphic on the domain (1). Indeed, at fixed
level and on a bounded parameter compact set, its expression
on the left of (14) has kernel \(O(A/B)\) at the negative
end and \(O(A^{-1})\) at the positive end. Here \(B\ne0\)
and its upper and lower bounds on that compact set are kept.
The original exact row tails therefore have precisely the
strict alias slopes (10), now at \(u=\beta\).
They give an integrable majorant uniform on that compact
set. The remaining bounded portion uses the holomorphic
right side of (14). This proves both local uniform
convergence and holomorphy of (15).

Equations (8)--(9) consequently give an exact decomposition
\[
\begin{split}
 H(c,x)&=S_N(c,x)+iN(B(c)-1)I_N(c,x),\\
 S_N(c,x)&=
 N\int_{L+ih}^{\beta+ih}T(a;c,x)\,da
       +2iN\int_{\mathbb R}w_h(t)T(\beta+it;c,x)\,dt .
\end{split}
\tag{16}
\]
Although the displayed main path uses \(\Re c,\Im c\),
the complete \(S_N\) is holomorphic: the first line of (16)
expresses it as a difference of holomorphic functions.
It agrees exactly with \(H\) at every admitted physical
total. These statements concern the complete expression,
not its separate path and current terms.

For \((c,x)\) near the actual \((c_*,x_0)\), the principal path in
(16) still has the original nonzero Gaussian. The modulus
comparison in equations (22)--(25) of the fixed-total note
extends to this symmetric interval: now
\[
       |2t-c_r|\le 2\beta-c_r<1
\]
on the whole path, and its midpoint and radii are unchanged.
Its symbol, action and \(N^{-1}\) power are consequently the
same. This does not estimate the remaining doubled current
in (16).

## 4. Exact cancellation under the complete outer sampling

Let \(\Gamma_c\) be a positively oriented bounded rectangle,
with real cuts \(\ell,u\) satisfying
\[
       2/3<\ell<u<\min(4/5,\beta),
\tag{17}
\]
neither cut a physical total index, and with finite lower
and upper heights of opposite signs. Denote by \(\mathcal M_N\)
the integers with \(\ell<m/N<u\).
Every admitted physical total is at most \(M_N\). By the
exact source identity,
\[
 V_{\mathcal M,N}(x)
   :=e^{2\pi i(N-1)x}\sum_{m\in\mathcal M_N}B_{N,m}(x)
    =e^{2\pi i(N-1)x}
           N\oint_{\Gamma_c}k_N(c)H(c,x)\,dc .
\tag{18}
\]
Both physical parities are retained.

The same sampling kernel gives
\[
                       k_N(c)(B(c)-1)=-1.
\tag{19}
\]
Since \(I_N\) is holomorphic throughout the entire rectangle,
its complete contour integral vanishes. Thus
\[
\boxed{\begin{split}
 V_{\mathcal M,N}(x)
   ={}&e^{2\pi i(N-1)x}N
                    \oint_{\Gamma_c}k_N(c)S_N(c,x)\,dc\\
   ={}&e^{2\pi i(N-1)x}N^2
        \oint_{\Gamma_c}k_N(c)
       \left\{\int_{L+ih}^{\beta+ih}T(a;c,x)\,da
           +2i\int_{\mathbb R}w_h(t)T(\beta+it;c,x)\,dt
       \right\}dc .
\end{split}}
\tag{20}
\]
This is a complete-cycle cancellation. Directly interchanging
the integral in (15) with this bounded outer contour is
also justified by its fixed-\(N\) uniform tail bounds.
It is not an interchange of two unbounded currents.

All four parts of \(\Gamma_c\) must remain together when using
(19). Its main integral, separate aliases and separate sides
need not individually annihilate the extra term. The outside
chirp, both densities \(N\), and the orientation of the
remaining right current are unchanged.

The full original adjacent source is exactly
\[
 V_{22,N}(x,x)=V_{\mathcal M,N}(x)
       +e^{2\pi i(N-1)x}\sum_{\substack{0\le m<N\\m\notin\mathcal M_N}}
                                      B_{N,m}(x).
\tag{21}
\]
No complementary physical total range is removed by (20).
Nor does this formula prove a lower bound for the complete
pair or its prescribed knot closing. Its analytic consequence
at present is a simpler exact endpoint obligation: on the
admitted full outer cycle the separate midpoint current can
be replaced by the doubled cutoff current in (16), while its
remaining total-period correction cancels exactly.
