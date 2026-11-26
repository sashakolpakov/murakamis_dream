# The original factorial symbol across a nonreal seam

Private research proof, 8 November 2026. The reciprocal factorial
used to interpolate the conditional rows has its original uniform
symbol across the line \(\Re y=0\), provided the imaginary part
stays strictly negative. This extends the regular row estimates to
the entire lower-left interval. It is a statement about the
factorial interpolant; the finite Fourier polynomial \(d_N\) must
still retain its separate forcing term and upper bound.

## 1. The interpolant and the compact domain

Use exactly the interpolant of
[Fourier-weight continuation, equations (3)--(4)](research_mixed_fourier_weight_continuation.md):
\[
 f_N(y)=\widehat P_N(Ny)^{-1},\qquad
 f_N(y+1/N)=\frac{f_N(y)}{1-e^{-2\pi i(y+1/N)}}.
 \tag{1}
\]
On every compact subset of \(0<\Re y<1\), its established
expansion is
\[
 f_N(y)=N^{-1/2}a_0(y)^{-1}e^{-Ng(y)}
                          (1+O_{\rm hol}(N^{-1})),
 \qquad
 a_0(y)=\sqrt{2\sin\pi y}\,e^{-i\pi y/2}.
 \tag{2}
\]
Both the action and the square root are the original ones.

Fix \(0<\delta<1/8\) and \(0<h_0<H_0<\infty\). We will
extend (2) to
\[
 \mathcal R=\{y:|\Re y|\le\delta,\ -H_0\le\Im y\le-h_0\}.
 \tag{3}
\]
All parameters are fixed before \(N\) tends to infinity.

In the lower half-plane the original functions continue as
\[
\begin{aligned}
 g(y)&=\frac{\operatorname{Li}_2(e^{-2\pi iy})-\pi^2/6}{2\pi i},
 &g'(y)&=\operatorname{Log}(1-e^{-2\pi iy}),\\
 a_0(y)&=e^{-i\pi/4}\exp\{g'(y)/2\}.
\end{aligned}
 \tag{4}
\]
The dilogarithm is given by its convergent power series because
\(|e^{-2\pi iy}|<1\). Thus these functions are holomorphic
through (3), and \(a_0\) never vanishes there. The identity
\[
                  1-e^{-2\pi iy}=2i e^{-i\pi y}\sin\pi y
 \tag{5}
\]
shows that the last line in (4) agrees with the square root
in (2), by continuation from the original strip. In particular
neither an action constant nor a square-root sign is reset.

## 2. A shift into the original strip

**Theorem 1.** Expansion (2), with its original functions (4),
holds uniformly on a fixed neighborhood of \(\mathcal R\),
with every fixed holomorphic derivative of its relative error
bounded by \(O(N^{-1})\).

**Proof.** Put
\[
          m_N=\lceil2\delta N\rceil,\qquad d_N^*=m_N/N.
 \tag{6}
\]
The symbol \(d_N^*\) here is a real displacement, distinct from
the Fourier polynomial \(d_N(Y)\). For all sufficiently large
\(N\), the shifted rectangle \(y+d_N^*\) lies in a fixed
compact subset of the original strip. For example its real
part lies in \([\delta,4\delta]\).

Iterating the exact recurrence (1), without dropping any
factor, gives
\[
 f_N(y)=
 \left\{\prod_{k=1}^{m_N}
       (1-e^{-2\pi i(y+k/N)})\right\}f_N(y+d_N^*).
 \tag{7}
\]
The product is nonzero on a fixed neighborhood of (3).
Equation (7) agrees with the original interpolant wherever
both sides were originally defined, and supplies its
holomorphic continuation across the seam. Using \(m_N+1\)
instead gives the same function by (1), so no new choice of
interpolant is involved.

Let \(L=g'\). The function \(L\) and its derivatives are
uniformly bounded on a fixed neighborhood of every segment
\([y,y+d_N^*]\) under consideration. The right-end sum has
the elementary trapezoidal expansion
\[
 \sum_{k=1}^{m_N}L(y+k/N)
 =N\{g(y+d_N^*)-g(y)\}
      +\frac{L(y+d_N^*)-L(y)}2+O(N^{-1}).
 \tag{8}
\]
For completeness, apply the trapezoidal rule to each interval
of length \(1/N\). Its integral remainder is bounded by a
constant times \(N^{-3}\sup|L''|\). Summing \(O(N)\)
intervals and multiplying by \(N\) gives the remainder in
(8). The argument is valid for a complex-valued analytic
function integrated along a real horizontal segment.

Exponentiation of (8) and substitution of (2) at the shifted
point in (7) give
\[
\begin{split}
 f_N(y)
  =N^{-1/2}e^{-Ng(y)}
    \frac{\exp\{[g'(y+d_N^*)-g'(y)]/2\}}
         {a_0(y+d_N^*)}\,(1+O(N^{-1})).
\end{split}
 \tag{9}
\]
The quotient in (9) equals \(a_0(y)^{-1}\) exactly by (4).
This proves (2) on the extended rectangle. The same proof
holds on a fixed larger rectangle still in the lower
half-plane. Cauchy's formula there proves the fixed
derivative bounds for the holomorphic relative error.
\(\square\)

The displacement in (6) depends on \(N\), but not on \(y\)
or any outside parameter. No differentiated integer cutoff
is introduced.

## 3. Consequence for the actual conditional rows

For \(\gamma=0,1\), the original factorial interpolation of
a row is
\[
 \mathcal R_{\gamma,N}(s;b,c)
 =e^{2\pi iNbs}
   \frac{\widehat P_N(N(b+s))\widehat P_N(N(c+s))}
        {\widehat P_N(Nb)\widehat P_N(Nc)
                        \widehat P_N(Ns)^{2+\gamma}}.
 \tag{10}
\]
At every physical row \(s=j/N\), the recurrence (1) gives
exactly
\[
 \mathcal R_{\gamma,N}(j/N;b,c)
  =\frac{B^{-j}p_j(B)p_j(C)}{P_j^{2+\gamma}},
 \quad B=e^{-2\pi ib},\quad C=e^{-2\pi ic}.
 \tag{11}
\]
The use of capital \(B,C\) in this equation denotes only
the two exponentiated boundary variables.

Suppose one of \(b,c\) belongs to (3), and every other
individual or summed argument in (10) lies in a fixed
compact subset of its original regular strip. Combining
Theorem 1 with the old expansions on those compact subsets
gives
\[
 \mathcal R_{\gamma,N}(s;b,c)
 =N^{-1-\gamma/2}\,
   \frac{a_0(b+s)a_0(c+s)}
        {a_0(b)a_0(c)a_0(s)^{2+\gamma}}\,
   e^{NQ_\gamma(s;b,c)}
                      (1+O_{\rm hol}(N^{-1})),
 \tag{12}
\]
where \(Q_\gamma\) is exactly the original phase, including
the chirp \(2\pi ibs\). The power of \(N\) follows from the
two numerator factors and the \(4+\gamma\) denominator
factors of \(\widehat P_N\). This is a row expansion; the
original factor \(+N\) is inserted only when the row is
integrated as the constant part of a half-grid contour.

In the lower-left attachment, take
\(-.102\le\Im y\le-.001\) and \(0\le\Re y\le.22\).
For the first conditional factor use \(b=a,c=y\); for
the next use \(b=y,c=z\). The retained real index cuts
are \(1/8,1/2\) in the first factor and
\(3/20,1/2\) or \(1/8,1/2\) in the next. All sums in (10)
then have real parts strictly between zero and one, with
a uniform separation from the two endpoints. The same
is true on every fixed finite-height contour between
these cuts. The only outer argument leaving the original
strip at \(q=0\) is \(y\), which Theorem 1 covers.

Thus the canonical row symbols and their fixed derivatives
remain uniform through this nonreal seam. Joining (3) to
the original regular-strip estimates covers the full
closed interval \(0\le\Re y\le.22\).

## 4. Keeping the Fourier polynomial distinct

Theorem 1 does not prove
\(d_N(e^{-2\pi iy})=f_N(y)(1+o(1))\) at the seam.
The original finite Fourier polynomial satisfies a forced
recurrence, whereas (1) is the factorial recurrence.
For the actual finite source, its full upper bound is the
separate one proved in
[the low physical-block theorem, Section 3](research_mixed_next_lower_left_low_physical_blocks.md):
\[
 |d_N(e^{-2\pi iy})|
       \le C_\tau N^{B_\tau}e^{N\{-\Re g(y)+\tau\}},
 \qquad \tau>0.
 \tag{13}
\]
The forcing is retained in that theorem.

Equations (12)--(13) justify combining the already established
joint profile bounds with the original canonical main
integrals all the way to \(q=0\). In particular the low-by-main
conclusion in Section 4 of the low physical-block theorem
extends from fixed \(q\ge\varepsilon>0\) to the full
closed lower-left interval, with its same conservative
exponential deficit. This concerns those specified
integrals and finite low blocks. The remaining upper
physical rows, last rows, contour remainders and noncentral
incoming pieces still require their own estimates.
