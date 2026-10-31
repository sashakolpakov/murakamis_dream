# An exact analytic function of the auxiliary colors

Fix an augmented plat diagram: a braid closed by specified cups and caps, with an auxiliary crossing circle around each retained twist region. At quantum level \(N\), the color \(n_i\in\{1,\ldots,N\}\) labels the representation on the \(i\)th auxiliary circle. The complete color is \(N\), and its deficit is \(h_i=N-n_i\).

This note constructs a particular entire function of the scaled deficits. It is a finite cosine sum whose coefficients are contractions of the original quantum operators. At physical high colors it gives exactly the complete-circle part of the invariant. The remaining terms are also specified by an exact identity. This construction is needed before complex stationary phase: an arbitrary interpolation of the integer color values would not preserve the quantum expression being estimated.

The finite formula works for every fixed augmented plat and both parities of \(N\). It gives exact Fourier reconstruction and a positive squared-norm identity. Those identities alone do not prove cancellation bounds or a nonzero geometric contribution. Such additional estimates are now established for the [strict Conway class](actual_conway_all_strict_tree_long_twist_volume.md) and other stated families; this note does not assert them for every plat.

## 1. Splitting one circle operator without losing derivatives

Let \(\Omega\) be the original Casimir operator on the pair of physical strands. Write \(T_n,U_n\) for the Chebyshev polynomials of the first and second kinds, normalized by \(T_0=1\), \(T_1(t)=t\), \(U_0=1\), and \(U_1(t)=2t\). The color-\(n\) circle operator is
\[
 L_n=(-1)^{n-1}U_{n-1}(\Omega/2),\qquad L_0=0.
\]
At level \(N\), the full pair algebra satisfies
\[
 P_N(\Omega)=2T_N(\Omega/2)+2=0.
\]
This polynomial relation includes repeated spectral nodes. Working in its quotient retains the first derivatives at those nodes, which the source notes call first normals. Merely recording the distinct eigenvalues would discard that information.

For every integer \(0\le h<N\), the exact circle identity is
\[
 L_{N-h}=(-1)^hT_h(\Omega/2)L_N+(-1)^NL_h. \tag{1}
\]
Indeed, the Chebyshev identity
\(U_{N-h-1}=T_hU_{N-1}-T_NU_{h-1}\), together with \(T_N=-1\) in the full quotient, gives (1). The first summand is called the core term and the second the alias term. These are names for the two terms of an operator identity; neither name implies an asymptotic estimate.

Put \(M=\lfloor(N-1)/2\rfloor\). The distinct spectral nodes are
\(c_j=2\cos((2j+1)\pi/N)\), for \(0\le j\le M\). Let \(L_{N,j}\) be the actual component of \(L_N\) at node \(c_j\), in every physical degree. The [complete compiler](actual_augmented_plat_phase_compiler.md) specifies these rank-one matrices and their derivative-derived coefficients. On the image of each component, multiplication by \(T_h(\Omega/2)\) acts by its value at \(c_j\): its derivative multiplies the complete-circle square-zero term and vanishes. Therefore
\[
 \begin{aligned}
 (-1)^hT_h(\Omega/2)L_N
   &=\sum_{j=0}^{M}\cos(\pi h m_j/N)L_{N,j},\\
 m_j&=N-2j-1.
 \end{aligned} \tag{2}
\]
The centering in (2) uses that \(h\) is an integer. The frequencies \(m_j\) are distinct, nonnegative, and all have parity \(N-1\). At an odd level, \(m_M=0\), so the last cosine equals one. No division by a vanishing endpoint sine is involved.

## 2. Defining the whole finite function

Fix the original augmented \(2k\)-plat skeleton and its \(b\) retained auxiliary circles. The number \(k\) records the plat width; \(b\) counts the color variables. At circle \(i\), retain the prescribed half twist \(R_i^{\epsilon_i}\), where \(\epsilon_i\in\{0,\pm1\}\), followed by the circle operator \(L_{N-h_i}\).

For a tuple \(\mathbf j=(j_1,\ldots,j_b)\), define \(A_N(\mathbf j)\) as follows: replace the \(i\)th circle operator by \(L_{N,j_i}\), retain \(R_i^{\epsilon_i}\), and perform the original marked contraction. Thus \(A_N\) includes the original cups, ordinary caps, unrestricted marked cap, pivotal factors and external scalar. It is a definite finite coefficient, not an unspecified boundary vector or normalization.

For \(\chi=(\chi_1,\ldots,\chi_b)\in\mathbb C^b\), set
\[
 C_N(\chi)=
 \sum_{j_1=0}^{M}\cdots\sum_{j_b=0}^{M}
 A_N(j_1,\ldots,j_b)
 \prod_{i=1}^{b}\cos(\pi m_{j_i}\chi_i). \tag{3}
\]
This is entire and even in each variable because the sum is finite. For a physical high-color tuple, \(0\le h_i\le M\), equation (2) shows that \(C_N(h/N)\) is exactly the contraction in which every circle uses its core term. At \(h=0\), every alias is \(L_0=0\), so \(C_N(0)\) is the full original complete-color scalar.

Let \(Z_N(h)\) denote the full marked scalar at those physical colors. Expanding (1) at all circles gives
\[
 Z_N(h)=C_N(h/N)
   +\sum_{\varnothing\ne S\subseteq\{1,\ldots,b\}}
       (-1)^{N|S|}Z_{N,S}(h). \tag{4}
\]
Here \(Z_{N,S}\) uses \(R_i^{\epsilon_i}L_{h_i}\) at every circle in \(S\), and the complete-image cosine factor of (2) at every other circle. The [all-color Hermite compiler](actual_mixed_augmented_plat_compiler.md) specifies each contraction, including the normal terms. Equation (4) retains all nonempty alias subsets; it does not say that they are smaller.

For a physical low color \(n\le\lfloor N/2\rfloor\), the usual physical decomposition instead sets its core to zero and takes the full ordinary coupon as its alias. Formula (3) still has values at the corresponding grid points, but they belong to its finite Fourier extension. They are not a redefinition of the physical low-color core. This distinction becomes important when estimating the color complement.

## 3. Recovering the coefficients and their squared norm

Define a frequency weight by \(w_j=1/2\) when \(m_j>0\), and \(w_j=1\) when \(m_j=0\). Direct summation gives the exact orthogonality relation
\[
 \frac1N\sum_{h=0}^{N-1}
 \cos(\pi h m_j/N)\cos(\pi h m_l/N)=w_j\delta_{jl}. \tag{5}
\]
To check it, expand the product into exponentials. The differences \(m_j-m_l\) are even integers of absolute value less than \(2N\). The sums \(m_j+m_l\) are also even; their only multiple of \(2N\) in this range is zero, occurring at the odd zero-frequency node. These observations give exactly the two weights above. No assumption that \(N\) is prime is used.

Applying (5) in each variable recovers the original contraction coefficients:
\[
 A_N(\mathbf j)=
 \frac{1}{N^b\prod_{i=1}^{b}w_{j_i}}
 \sum_{h_1=0}^{N-1}\cdots\sum_{h_b=0}^{N-1}
 C_N(h/N)\prod_{i=1}^{b}\cos(\pi h_i m_{j_i}/N). \tag{6}
\]
The corresponding Parseval identity is
\[
 \frac1{N^b}\sum_{h_1=0}^{N-1}\cdots\sum_{h_b=0}^{N-1}|C_N(h/N)|^2
 =\sum_{j_1=0}^{M}\cdots\sum_{j_b=0}^{M}
      \left(\prod_{i=1}^{b}w_{j_i}\right)|A_N(\mathbf j)|^2. \tag{7}
\]
For fixed \(b\), the transform costs only a power of \(N\). However, (7) measures squared magnitudes. It does not make the signed sum \(C_N(0)=\sum_{\mathbf j}A_N(\mathbf j)\) positive or prove that its geometric contribution is nonzero.

### The opposite endpoint and the limits of periodicity

Let \(e_i\) be the \(i\)th coordinate vector. Since all frequencies have the same parity, the finite function obeys
\[
 \begin{aligned}
 C_N(\chi+e_i)&=(-1)^{N-1}C_N(\chi),\\
 C_N(\chi_1,\ldots,-\chi_i,\ldots,\chi_b)
   &=C_N(\chi_1,\ldots,\chi_i,\ldots,\chi_b).
 \end{aligned} \tag{8}
\]
Thus it is periodic at odd levels and antiperiodic at even levels. Values near the grid endpoint \(h_i=N\) reflect values near \(h_i=0\).

There is a conditional consequence for a proposed global estimate of this extension. Suppose a fixed-neighborhood analytic asymptotic has complete rate \(F_0\) and an amplitude that is not identically zero near the origin. Choose arbitrarily small fixed positive real arguments where the amplitude is nonzero. Nearby grid values have rates arbitrarily close to \(F_0\), and (8) reflects them outside the near-zero neighborhood. Hence this Fourier extension cannot have a fixed exponential gap on the whole complementary cube. If the amplitude is nonzero at zero itself, the sample \(h=1\) already has the complete rate and reflects to \(h=N-1\). That particular moving-sample argument needs nonvanishing at zero, not merely a nonzero analytic function nearby.

Periodicity by itself does not give this obstruction. In one variable, the exact reproducing kernel is
\[
 \sum_{j=0}^{M}w_j^{-1}\cos(\pi m_j\chi)
 =\sum_{r=0}^{N-1}e^{\pi i(N-1-2r)\chi}
 =\frac{\sin(N\pi\chi)}{\sin(\pi\chi)}. \tag{8a}
\]
At \(\chi=h/N\), for \(0\le h<N\), its value is \(N\delta_{h,0}\) at both parities. Multiplying by \(e^{NF_0}/N\) gives complete rate \(F_0\) and zero at every other sample. This example has no fixed-scale analytic neighborhood of the required asymptotic form. It explains why the additional hypothesis, and the physical distinction after (4), must be retained.

Finally, the elementary inequality \(|\cos z|\le e^{|\operatorname{Im}z|}\) gives
\[
 |C_N(\chi)|\le
 e^{\pi(N-1)\sum_i|\operatorname{Im}\chi_i|}
 \sum_{\mathbf j}|A_N(\mathbf j)|. \tag{9}
\]
This exact estimate has a linear cost in complex height. The quadratic height control needed for a filling saddle is a stronger analytical statement.

## 4. What this finite construction supplies

Formula (3) specifies a regular continuation even at the odd zero-frequency endpoint. Within its stated cosine span it is uniquely determined by the grid values. It does not replace a generic-quantum-parameter germ of the whole pointed invariant.

For a general fixed plat, using this function in a filling proof still requires a uniform asymptotic on a fixed complex neighborhood, a selected contribution on the original integration cycle, bounds for all physical alias terms and far colors, and the actual marked geometric regulator. The complete and mixed compilers expose those quantities but do not themselves estimate them. The twist threshold is attached to the fixed diagram; the frequency scale \(N\) remains the quantum level.

The [finite check](../experiments/audit_actual_augmented_plat_entire_core_color_packet.py) tests the full-algebra split, the centered characters, the tensor Fourier identities and the reproducing-kernel example. Its recorded cases include 162 signed split identities, 204 centered characters and 27 tensor Fourier packets. The proofs above, rather than the number of cases, establish the general identities and their stated limitations.
